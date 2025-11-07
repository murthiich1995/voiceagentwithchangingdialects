"""Voice input module for speech recognition."""
import speech_recognition as sr


class VoiceInput:
    """Handles voice input and converts speech to text."""

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self, timeout=5, phrase_time_limit=10):
        """
        Listen for voice input and convert to text.

        Args:
            timeout: Maximum time to wait for speech to start (seconds)
            phrase_time_limit: Maximum time for a phrase (seconds)

        Returns:
            str: Transcribed text from speech, or None if failed
        """
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening... Speak now!")

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )
                print("Processing speech...")

                # Using Google's speech recognition
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text

            except sr.WaitTimeoutError:
                print("No speech detected within timeout period.")
                return None
            except sr.UnknownValueError:
                print("Could not understand the audio.")
                return None
            except sr.RequestError as e:
                print(f"Speech recognition service error: {e}")
                return None
            except Exception as e:
                print(f"Error during speech recognition: {e}")
                return None
