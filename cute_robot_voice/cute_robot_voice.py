from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.effects import low_pass_filter
from pydub.generators import Sine
import numpy as np
import simpleaudio as sa
from scipy.signal import convolve

def generate_speech(text):
    tts = gTTS(text)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return AudioSegment.from_file(fp, format="mp3")

def pitch_shift(sound, semitones):
    rate = sound.frame_rate * (2.0 ** (semitones / 12.0))
    return sound._spawn(sound.raw_data, overrides={'frame_rate': int(rate)}).set_frame_rate(sound.frame_rate)

def add_reverb(sound):
    impulse = AudioSegment.silent(duration=100) + Sine(1000).to_audio_segment(duration=50).fade_in(50).fade_out(50)
    convolved = convolve(np.array(sound.get_array_of_samples()), np.array(impulse.get_array_of_samples()), mode='full')[:len(sound)]
    max_val = np.iinfo(np.int16).max
    convolved = np.clip(convolved / np.max(np.abs(convolved)), -1, 1) * max_val
    return sound._spawn(data=convolved.astype(np.int16).tobytes())

def apply_cute_robot_effect(sound):
    cute_sound = pitch_shift(sound, 7)
    cute_sound = low_pass_filter(cute_sound, cutoff=3000)
    cute_sound = add_reverb(cute_sound)
    return cute_sound

def play_sound(sound):
    play_obj = sa.play_buffer(
        sound.raw_data,
        num_channels=sound.channels,
        bytes_per_sample=sound.sample_width,
        sample_rate=sound.frame_rate
    )
    play_obj.wait_done()

def apply_and_play_effect(sound):
    cute_robot_voice = apply_cute_robot_effect(sound)
    play_sound(cute_robot_voice)
