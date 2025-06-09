# CrewAI Orchestration Demo

A simple demonstration of AI agent orchestration using CrewAI framework. This project shows how multiple specialized agents can work together to analyze technology trends and translate technical concepts into accessible language.

## What it does

The system uses two AI agents:
- A Research Agent that identifies emerging technology trends
- A Communication Agent that translates technical information into easy-to-understand explanations

## Requirements

- Python 3.10+
- OpenAI API key

## Quick Start

1. Set up environment variables:
```
# OpenAI configuration
OPENAI_API_KEY=your_api_key
OPENAI_MODEL_NAME=o3-mini-2025-01-31

# Gemini configuration (optional)
GEMINI_API_KEY=your_gemini_api_key
MODEL_NAME_GEMINI=models/gemini-2.5-flash-preview-05-20
```

2. Install dependencies:

Using Poetry (recommended):
```bash
poetry install
```

Or with pip:
```bash
pip install -r requirements.txt
```

3. Run the demo:

Original version:
```bash
python tech_trends_crew.py
```

Modularized version:
```bash
python crew.py
```

### Note on Multi-Model Setup
The modularized version supports using different models for each agent:
- The Research Agent uses OpenAI's model
- The Communication Agent uses Google's Gemini model

To modify which models are used, edit the `agents.py` file.

## Output

The script will generate a technical analysis of emerging technology trends and a simplified explanation suitable for non-technical audiences.
