import os
from pydantic import BaseModel

from crewai.flow import Flow, listen, start

from src.crewai_project.crew import ResearchCrew

# Configure Ollama as the LLM provider for CrewAI
os.environ["OPENAI_API_BASE"] = "http://localhost:11434/v1"
os.environ["OPENAI_MODEL_NAME"] = "llama3.1:8b"
os.environ["OPENAI_API_KEY"] = "NA"

class ResearchFlowState(BaseModel):
  topic: str = ""
  report: str = ""


class LatestAiFlow(Flow[ResearchFlowState]):
  @start()
  def prepare_topic(self, crewai_trigger_payload: dict | None = None):
    if crewai_trigger_payload:
      self.state.topic = crewai_trigger_payload.get("topic", "Artificial Intelligence")
    else:
      self.state.topic = "Artificial Intelligence"
    print(f"Topic: {self.state.topic}")

  @listen(prepare_topic)
  def run_research(self):
    print(f"Starting research on topic: {self.state.topic} using Ollama Llama3.1:8b and Tavily search...")
    result = ResearchCrew().crew().kickoff(inputs={"topic": self.state.topic})
    self.state.report = result.raw
    print("Research crew finished.")

  @listen(run_research)
  def summarize(self):
    print("Report generated successfully. You can find it at: output/report.md")


def kickoff():
  LatestAiFlow().kickoff()


def plot():
  LatestAiFlow().plot()


if __name__ == "__main__":
  kickoff()