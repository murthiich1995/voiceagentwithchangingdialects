"""Voice output module for text-to-speech."""
import os
from gtts import gTTS
import pygame
import tempfile


class VoiceOutput:
    """Handles text-to-speech conversion and audio playback."""

    def __init__(self):
        """Initialize the voice output system."""
        pygame.mixer.init()

    def speak(self, text, lang='en', slow=False):
        """
        Convert text to speech and play it.

        Args:
            text: The text to speak
            lang: Language code (default: 'en' for English)
            slow: Whether to speak slowly (default: False)
        """
        try:
            print(f"Speaking: {text}")

            # Generate speech
            tts = gTTS(text=text, lang=lang, slow=slow)

            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
                temp_file = fp.name
                tts.save(temp_file)

            # Play the audio
            pygame.mixer.music.load(temp_file)
            pygame.mixer.music.play()

            # Wait for playback to finish
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            # Clean up
            pygame.mixer.music.unload()
            os.remove(temp_file)

        except Exception as e:
            print(f"Error during text-to-speech: {e}")

    def speak_response(self, response_dict):
        """
        Speak a response from the dialect agent.

        Args:
            response_dict: Dictionary with 'dialect' and 'response' keys
        """
        if isinstance(response_dict, dict):
            text = response_dict.get('response', str(response_dict))
        else:
            text = str(response_dict)

        self.speak(text)
