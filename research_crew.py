from crewai import Crew
from tasks.research_task import create_research_task
from tasks.summarize_task import create_summary_task

def build_research_crew(topic: str) -> Crew:
    research_task = create_research_task(topic)
    summary_task = create_summary_task()

    return Crew(
        agents=[
            research_task.agent,
            summary_task.agent
        ],
        tasks=[
            research_task,
            summary_task
        ],
        process="sequential",
        verbose=True
    )
