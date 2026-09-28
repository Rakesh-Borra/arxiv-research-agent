---
title: Autonomous arXiv Research Assistant
emoji: 🔎
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 6.27.0
app_file: app.py
pinned: false
license: mit
---

# Autonomous arXiv Research Assistant

An AI-powered research assistant that searches arXiv for academic papers and helps users summarize, compare, and generate citations for research papers.

This project was developed for **CS 697 – Industry AI Applications Lab at UMass Boston**.

## Features

- Search for academic papers directly from arXiv
- Retrieve recent and relevant research papers
- Summarize research papers
- Compare multiple papers and their approaches
- Generate BibTeX citations
- Provide paper metadata including title, authors, year, and arXiv URL
- Avoid generating fictional papers when no matching results are found
- Interactive web interface built with Gradio

## How It Works

The application follows a simple agentic AI workflow:

```text
User
  ↓
Gradio Interface
  ↓
CodeAgent
  ↓
Qwen 2.5 Coder
  ↓
arXiv Search Tool
  ↓
Research Papers
  ↓
Agent processes the results
  ↓
Response displayed in Gradio
```

The AI agent decides when and how to use the arXiv search tool based on the user's request.

## Technologies

- Python
- Gradio
- Hugging Face smolagents
- Qwen 2.5 Coder
- arXiv API

## Example Prompts

```text
Find 3 recent papers about AI agents and summarize them.
```

```text
Find 2 papers about computer vision and compare their approaches,
key differences, and applications.
```

```text
Find 2 recent papers about LLM agents and format them as BibTeX.
```

## Running Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Authenticate with Hugging Face if required:

```bash
hf auth login
```

Run the application:

```bash
python3 app.py
```

Then open the local Gradio URL shown in the terminal.

## Project Files

- `app.py` – AI agent configuration and Gradio interface
- `tools.py` – arXiv paper search tool
- `requirements.txt` – Python dependencies
- `README.md` – project documentation

## Author

**Rakesh Borra**  
M.S. Computer Science  
University of Massachusetts Boston