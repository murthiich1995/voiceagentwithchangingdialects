# Voice Agent with Dialect Adaptation

A voice agent that identifies the user's slang and dialect from their speech and responds in the same style.

## Features

- Voice input recognition (speech-to-text)
- Dialect and slang identification
- Dynamic response generation matching user's dialect
- Voice output (text-to-speech)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your Anthropic API key
```

3. Run the agent:
```bash
python main.py
```

## Usage

Simply speak a greeting, and the agent will:
1. Convert your speech to text
2. Identify your dialect/slang
3. Generate a greeting response in the same dialect
4. Speak the response back to you

## Examples

- Input: "Yo, what's good?" → Response: "Yo! What's good with you, fam?"
- Input: "G'day mate!" → Response: "G'day! How ya going, mate?"
- Input: "Howdy y'all!" → Response: "Howdy partner! How y'all doing?"
