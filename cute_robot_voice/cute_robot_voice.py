from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.effects import speedup, low_pass_filter
from pydub.generators import Sine
import numpy as np
import simpleaudio as sa
from scipy.signal import convolve

# Function to generate speech using gTTS
def generate_speech(text):
    tts = gTTS(text)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return AudioSegment.from_file(fp, format="mp3")

# Function to apply pitch shift
def pitch_shift(sound, semitones):
    rate = sound.frame_rate * (2.0 ** (semitones / 12.0))
    return sound._spawn(sound.raw_data, overrides={'frame_rate': int(rate)}).set_frame_rate(sound.frame_rate)

# Function to add reverb
def add_reverb(sound):
    # Creating a simple reverb effect using convolution
    impulse = AudioSegment.silent(duration=100) + Sine(1000).to_audio_segment(duration=50).fade_in(50).fade_out(50)
    convolved = convolve(
        np.array(sound.get_array_of_samples()),
        np.array(impulse.get_array_of_samples()),
        mode='full'
    )
    convolved = convolved[:len(sound)]
    
    # Normalize and clip the convolved result to avoid invalid values
    max_val = np.iinfo(np.int16).max
    min_val = np.iinfo(np.int16).min
    max_abs_val = np.max(np.abs(convolved))
    if max_abs_val > 0:
        convolved = np.clip(convolved, min_val, max_val)
        convolved = convolved / max_abs_val * max_val
    else:
        # If max_abs_val is 0, return the original sound without reverb
        return sound
    
    return sound._spawn(data=convolved.astype(np.int16).tobytes())

# Function to apply cute robot effect
def apply_cute_robot_effect(sound):
    # Apply pitch shift to make it sound cute
    cute_sound = pitch_shift(sound, 7)

    # Apply low-pass filter to soften the sound
    cute_sound = low_pass_filter(cute_sound, cutoff=3000)

    # Add reverb for an echo-like effect
    cute_sound = add_reverb(cute_sound)

    return cute_sound

# Function to play sound
def play_sound(sound):
    play_obj = sa.play_buffer(
        sound.raw_data,
        num_channels=sound.channels,
        bytes_per_sample=sound.sample_width,
        sample_rate=sound.frame_rate
    )
    play_obj.wait_done()

def speak(text):
    # Apply and play cute robot effect
    robot_voice = apply_cute_robot_effect(generate_speech(text))
    play_sound(robot_voice)
