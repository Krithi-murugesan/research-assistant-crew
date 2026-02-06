from crewai import Task
from agents.researcher import create_researcher_agent

def create_research_task(topic: str) -> Task:
    return Task(
        description=(
            f"Research the topic '{topic}'. "
            "Cover key concepts, architecture, real-world use cases, "
            "recent trends, and limitations. "
            "Structure the response using markdown headers."
        ),
        expected_output="A well-structured markdown research report.",
        agent=create_researcher_agent()
    )
