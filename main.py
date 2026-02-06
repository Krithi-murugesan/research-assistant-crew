import argparse
import os
from core.config import Settings
from core.logging import setup_logger
from core.exceptions import CrewExecutionError
from crew.research_crew import build_research_crew

logger = setup_logger("main")

def run(topic: str):
    Settings.validate()

    crew = build_research_crew(topic)

    try:
        logger.info(f"Starting research for topic: {topic}")
        result = crew.kickoff()

        os.makedirs(Settings.OUTPUT_DIR, exist_ok=True)

        with open(f"{Settings.OUTPUT_DIR}/research_report.md", "w") as f:
            f.write(result[0])

        with open(f"{Settings.OUTPUT_DIR}/summary.txt", "w") as f:
            f.write(result[1])

        logger.info("Research pipeline completed successfully")

    except Exception as e:
        logger.exception("Crew execution failed")
        raise CrewExecutionError(str(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Production-grade Research Assistant Crew"
    )
    parser.add_argument(
        "--topic",
        type=str,
        required=True,
        help="Topic to research"
    )
    args = parser.parse_args()

    run(args.topic)
