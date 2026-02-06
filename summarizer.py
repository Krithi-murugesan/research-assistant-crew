from crewai import Agent

def create_summarizer_agent() -> Agent:
    return Agent(
        role="Summarizer",
        goal="Produce concise, high-signal summaries",
        backstory="Specialist in distilling complex research into executive-friendly bullet points.",
        verbose=True
    )
