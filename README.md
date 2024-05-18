# Cute Robot Voice

Cute Robot Voice is a Python package that allows you to generate cute robot voices using text-to-speech synthesis and apply various effects to them.

## Installation

You can install Cute Robot Voice via pip:

```bash
pip install cute-robot-voice
```

## Usage

### Generating Cute Robot Voice

To generate a cute robot voice from text, use the `generate_speech` function:

```python
from cute_robot_voice import generate_speech

# Generate speech
text = "Hello, I am a cute robot."
speech = generate_speech(text)
```

### Applying Cute Robot Effect and Playing

To apply the cute robot effect and play the generated voice, use the `apply_and_play_effect` function:

```python
from cute_robot_voice import apply_and_play_effect

# Apply cute robot effect and play
apply_and_play_effect(speech)
```

### Additional Effects

You can also apply individual effects separately:

```python
from cute_robot_voice import apply_cute_robot_effect, play_sound

# Apply cute robot effect
cute_robot_voice = apply_cute_robot_effect(speech)

# Play the cute robot voice
play_sound(cute_robot_voice)
```

## Documentation

For more information and detailed documentation, please refer to the [documentation](https://github.com/Tushar552/cute_robot_voice).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README.md file provides a brief overview of the Cute Robot Voice package, installation instructions, usage examples, links to documentation, and license information. Feel free to customize it further according to your package's specifics and requirements. If you have any further questions or need assistance, feel free to ask!