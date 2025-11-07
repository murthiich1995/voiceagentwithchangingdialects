"""Main application for the voice agent with dialect adaptation."""
import os
from dotenv import load_dotenv
from voice_input import VoiceInput
from voice_output import VoiceOutput
from dialect_agent import DialectAgent


def main():
    """Run the voice agent with dialect adaptation."""
    # Load environment variables
    load_dotenv()

    print("=" * 60)
    print("Voice Agent with Dialect Adaptation")
    print("=" * 60)
    print("\nInitializing...")

    try:
        # Initialize components
        voice_input = VoiceInput()
        voice_output = VoiceOutput()
        agent = DialectAgent()

        print("\n✓ All components initialized successfully!")
        print("\nHow it works:")
        print("1. Speak a greeting when prompted")
        print("2. The agent will identify your dialect/slang")
        print("3. The agent will respond in the same dialect")
        print("\nPress Ctrl+C to exit\n")

        while True:
            print("-" * 60)
            # Get voice input
            user_text = voice_input.listen()

            if user_text:
                # Get response from agent
                result = agent.identify_and_respond(user_text)

                print(f"\n[Detected dialect: {result['dialect']}]")
                print(f"Agent: {result['response']}\n")

                # Speak the response
                voice_output.speak(result['response'])
            else:
                print("No input detected. Please try again.\n")

    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋")
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you have:")
        print("1. Set ANTHROPIC_API_KEY in .env file")
        print("2. Installed all requirements: pip install -r requirements.txt")
        print("3. A working microphone connected")


if __name__ == "__main__":
    main()
