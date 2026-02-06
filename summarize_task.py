from crewai import Task
from agents.summarizer import create_summarizer_agent

def create_summary_task() -> Task:
    return Task(
        description=(
            "Summarize the research into concise bullet points. "
            "Focus on clarity, impact, and decision-making value."
        ),
        expected_output="High-quality bullet point summary.",
        agent=create_summarizer_agent()
    )
