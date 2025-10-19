from google.adk.agents import LlmAgent
from dotenv import load_dotenv

load_dotenv()
GEMINI_MODEL = "gemini-2.5-flash"
agent2 = LlmAgent(
    name="Agent2",
    model=GEMINI_MODEL,
    description="",
    instruction="",
    tools=[]
)


