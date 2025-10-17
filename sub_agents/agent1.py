from google.adk.agents import LlmAgent
from dotenv import load_dotenv

load_dotenv()
GEMINI_MODEL = "gemini-2.5-flash"
agent1 = LlmAgent(
    name="Agent1",
    model=GEMINI_MODEL,
    description="",
    instructions="",
    tools=[]
)


