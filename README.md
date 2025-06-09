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
OPENAI_API_KEY=your_api_key
MODEL_NAME_OPENAI=o3-mini-2025-01-31
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

With Poetry:
```bash
poetry run python tech_trends_crew.py
```

Or directly:
```bash
python tech_trends_crew.py
```

## Output

The script will generate a technical analysis of emerging technology trends and a simplified explanation suitable for non-technical audiences.
