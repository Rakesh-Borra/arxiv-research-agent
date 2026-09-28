import os
import gradio as gr

from dotenv import load_dotenv
from smolagents import CodeAgent, InferenceClientModel
from tools import search_arxiv


# Load environment variables
load_dotenv(".env")

HF_TOKEN = os.getenv("HF_TOKEN")


# Initialize the Qwen model
model = InferenceClientModel(
    model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    token=HF_TOKEN
)


# Create the AI Research Assistant
agent = CodeAgent(
    tools=[search_arxiv],
    model=model,
    add_base_tools=False,
    max_steps=5,
    instructions="""
You are an AI Research Assistant that helps users discover and understand
academic papers from arXiv.


Use the search_arxiv tool whenever the user asks for academic papers.

Guidelines:
- If the user asks for recent or newest papers, search using sort_by="recent".
- Otherwise, search using sort_by="relevance".
- Summarize papers clearly and concisely when requested.
- Compare papers when the user asks for a comparison.
- Generate BibTeX-style citations when requested.
- Include paper titles, authors, year, and arXiv URL when appropriate.
- Never invent papers or paper metadata. Use information returned by search_arxiv.


Output formatting:
- Format responses using clean Markdown.
- Use headings when presenting multiple sections.
- For paper results, clearly separate each paper.
- Use bullet points for authors, year, summary, and URL.
- When comparing papers, use clear sections for Approach, Key Differences, and Applications.
- When generating BibTeX, put each citation inside a separate Markdown code block.
- If no papers are found, clearly say that no matching papers were found.
- Never create hypothetical or fictional papers, authors, URLs, or citations.
"""
)


# Send the user's request to the AI agent
def agent_chat(user_input):
    return agent.run(user_input)


# Create the Gradio web interface
demo = gr.Interface(
    fn=agent_chat,

    inputs=gr.Textbox(
        lines=3,
        placeholder=(
            "Try: Find 3 recent papers about AI agents and summarize them."
        )
    ),

    outputs=gr.Markdown(
        label="Research Assistant Output"
    ),

    title="Autonomous arXiv Research Assistant",

    description=(
        "Search, summarize, compare, and generate citations "
        "for academic papers from arXiv using an AI agent."
    ),

    examples=[
        ["Find 3 recent papers about AI agents and summarize them."],
        ["Find 2 papers about computer vision and compare them."],
        ["Find 2 recent papers about LLM agents and format them as BibTeX."]
    ]
)


# Start the application
if __name__ == "__main__":
    demo.launch()