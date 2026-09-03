# EZ-DOC.AI

> **Historical GenAI prototype.** This repository captures an earlier experiment in LLM-assisted document generation using Cohere and Flask. It is preserved as part of my engineering progression and is not positioned as a current production system.

## What it explores

EZ-DOC.AI takes a user prompt, sends it to a language model, and turns the generated response into a downloadable `.docx` document through a lightweight web application.

The project explores a simple end-to-end GenAI flow:

```text
User prompt
    ↓
Flask application
    ↓
Cohere generation
    ↓
Document assembly
    ↓
DOCX output
```

## Features

- prompt-driven document generation,
- Cohere API integration,
- Flask-based web interface,
- `.docx` document generation,
- configurable local resource paths.

## Setup

```bash
git clone https://github.com/showman-sharma/EZ-DOC.AI.git
cd EZ-DOC.AI
pip install -r requirements.txt
```

Create a local configuration from the safe example:

```bash
cp config/config.example.json config/config.json
```

Then replace `YOUR_COHERE_API_KEY` with your own key and adjust any local resource paths.

> Never commit API keys, certificates, private keys, or other credentials. `config/config.json` and `*.pem` files are excluded from version control.

## Run

```bash
python app.py
```

Then open the local Flask application in your browser.

## Why I keep this repository

This project predates the more mature RAG, agentic, evaluation, and reasoning systems in my current portfolio. I keep it public because it shows an earlier stage of moving from isolated model experimentation toward **complete AI-powered application workflows**.

For newer work, see:

- [agentic_rag](https://github.com/showman-sharma/agentic_rag)
- [ai_blog_workflow](https://github.com/showman-sharma/ai_blog_workflow)
- [drug_ae_reasoner](https://github.com/showman-sharma/drug_ae_reasoner)

## License

MIT License. See [`LICENSE`](LICENSE).
