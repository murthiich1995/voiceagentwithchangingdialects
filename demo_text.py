"""Text-based demo of the dialect agent (no voice required)."""
import os
from dotenv import load_dotenv
from dialect_agent import DialectAgent


def main():
    """Run a text-based demo of the dialect agent."""
    # Load environment variables
    load_dotenv()

    print("=" * 60)
    print("Dialect Agent - Text Demo")
    print("=" * 60)
    print("\nThis demo shows how the agent identifies and responds to")
    print("different dialects and slang without requiring voice input.\n")

    try:
        agent = DialectAgent()
        print("✓ Agent initialized!\n")

        # Example greetings in different dialects
        examples = [
            "Yo, what's good?",
            "G'day mate!",
            "Howdy y'all!",
            "Oi, what's up bruv?",
            "Hiya! How are you doing?",
            "Sup dude?",
            "Hey fam, how you been?",
            "What's crackin'?",
        ]

        print("Running example greetings...\n")
        print("-" * 60)

        for example in examples:
            print(f"\nUser: {example}")
            result = agent.identify_and_respond(example)
            print(f"Dialect: {result['dialect']}")
            print(f"Agent: {result['response']}")
            print("-" * 60)

        # Interactive mode
        print("\n\nInteractive Mode - Type your own greetings!")
        print("(Type 'quit' to exit)\n")

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\nGoodbye! 👋")
                break

            if not user_input:
                continue

            result = agent.identify_and_respond(user_input)
            print(f"[Dialect: {result['dialect']}]")
            print(f"Agent: {result['response']}\n")

    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure you have:")
        print("1. Created a .env file with your ANTHROPIC_API_KEY")
        print("2. Installed requirements: pip install -r requirements.txt")


if __name__ == "__main__":
    main()
