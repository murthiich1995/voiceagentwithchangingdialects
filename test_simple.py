"""Simple test to verify the dialect agent works."""
import os
import json
from anthropic import Anthropic

# For testing purposes, let's use a simple example
print("Testing dialect agent core functionality...\n")

# Check if API key is available
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key or api_key == "your_api_key_here":
    print("⚠️  No valid API key found.")
    print("\nTo run this demo with real API calls, you need to:")
    print("1. Get an API key from https://console.anthropic.com/")
    print("2. Set it in .env file: ANTHROPIC_API_KEY=your_actual_key")
    print("\nShowing example output instead:\n")
    print("=" * 60)

    # Show mock examples
    examples = [
        ("Yo, what's good?", "Urban/Hip-hop slang", "Yo! What's good with you, fam?"),
        ("G'day mate!", "Australian English", "G'day! How ya going, mate?"),
        ("Howdy y'all!", "Southern American English", "Howdy partner! How y'all doing today?"),
        ("Oi, what's up bruv?", "British English slang", "Alright bruv! What's happening?"),
        ("Hiya! How are you doing?", "Standard British English", "Hiya! I'm doing well, thanks! How about you?"),
    ]

    for user_input, dialect, response in examples:
        print(f"\nUser: {user_input}")
        print(f"Dialect: {dialect}")
        print(f"Agent: {response}")
        print("-" * 60)
else:
    print("✓ API key found! Testing with real API calls...\n")
    from dialect_agent import DialectAgent

    try:
        agent = DialectAgent()

        examples = [
            "Yo, what's good?",
            "G'day mate!",
            "Howdy y'all!",
        ]

        for user_input in examples:
            print(f"\nUser: {user_input}")
            result = agent.identify_and_respond(user_input)
            print(f"Dialect: {result['dialect']}")
            print(f"Agent: {result['response']}")
            print("-" * 60)
    except Exception as e:
        print(f"Error: {e}")
