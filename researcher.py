from crewai import Agent

def create_researcher_agent() -> Agent:
    return Agent(
        role="Researcher",
        goal="Conduct accurate, structured research on a given topic",
        backstory="Expert research analyst skilled at synthesizing reliable information.",
        verbose=True
    )
