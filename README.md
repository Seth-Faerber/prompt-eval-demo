# Prompt Eval Demo

A minimal CLI for testing prompts with Claude.

## Quick Start

### 1. Activate the virtual environment

```bash
source .venv/bin/activate
```

Your terminal prompt will change to show `(.venv)` — this means you're using the project's isolated Python.

### 2. Install dependencies (first time only)

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Open `.env` and replace `your-key-here` with your [Anthropic API key](https://console.anthropic.com/).

### 4. Run the app

```bash
python main.py
```

Type a prompt, get Claude's response. Type `quit` or `exit` to stop.

## Project Structure

```
.env                 # Your API key (git-ignored)
.venv/               # Virtual environment (git-ignored)
main.py              # The app — single file, ~70 lines
requirements.txt     # Python dependencies
```
