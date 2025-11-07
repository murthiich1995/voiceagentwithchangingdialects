"""Dialect identification and response generation using Claude."""
import os
from anthropic import Anthropic


class DialectAgent:
    """Agent that identifies dialect/slang and generates matching responses."""

    def __init__(self, api_key=None):
        """
        Initialize the dialect agent.

        Args:
            api_key: Anthropic API key. If None, reads from ANTHROPIC_API_KEY env var
        """
        if api_key is None:
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError(
                    "API key not provided. Set ANTHROPIC_API_KEY environment variable "
                    "or pass api_key parameter."
                )

        self.client = Anthropic(api_key=api_key)

    def identify_and_respond(self, user_input):
        """
        Identify the dialect/slang in user input and generate a greeting response.

        Args:
            user_input: The user's greeting text

        Returns:
            dict: Contains 'dialect' and 'response' keys
        """
        system_prompt = """You are a dialect and slang expert. Your task is to:
1. Identify the dialect, slang, or regional speaking style in the user's greeting
2. Generate a friendly greeting response that matches their exact dialect and slang

Be authentic and natural. Match their energy and style precisely.

Respond in this JSON format:
{
  "dialect": "description of the dialect/slang (e.g., 'Urban/Hip-hop slang', 'Australian English', 'Southern American English')",
  "response": "your greeting response in the same dialect"
}"""

        user_prompt = f"User greeting: \"{user_input}\"\n\nIdentify the dialect and respond with a matching greeting."

        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=1024,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_prompt}
                ]
            )

            response_text = message.content[0].text

            # Parse the response
            import json
            # Try to extract JSON from the response
            if "```json" in response_text:
                json_start = response_text.find("```json") + 7
                json_end = response_text.find("```", json_start)
                response_text = response_text[json_start:json_end].strip()
            elif "```" in response_text:
                json_start = response_text.find("```") + 3
                json_end = response_text.find("```", json_start)
                response_text = response_text[json_start:json_end].strip()

            result = json.loads(response_text)

            return {
                "dialect": result.get("dialect", "Unknown"),
                "response": result.get("response", "Hello!")
            }

        except json.JSONDecodeError:
            # If JSON parsing fails, try to extract the response directly
            return {
                "dialect": "Unable to identify",
                "response": response_text.strip()
            }
        except Exception as e:
            print(f"Error calling Claude API: {e}")
            return {
                "dialect": "Unknown",
                "response": "Hello! Nice to meet you!"
            }

    def chat(self, user_input):
        """
        Simple chat interface that identifies dialect and responds.

        Args:
            user_input: The user's message

        Returns:
            str: The response in matching dialect
        """
        result = self.identify_and_respond(user_input)
        print(f"\n[Detected dialect: {result['dialect']}]")
        return result['response']
