from google.adk.agents import LlmAgent
from sub_agents.agent1 import agent1
from sub_agents.agent2 import agent2
from sub_agents.agent3 import agent3
from sub_agents.agent4 import agent4
from dotenv import load_dotenv

load_dotenv()
GEMINI_MODEL = "gemini-2.5-flash"
root_agent = LlmAgent(
    name="Orchestra",
    model=GEMINI_MODEL,
    description="You are orchestrating agent that directs the user request to the suitable agent",
    instructions="You are an agent that understands the user input and calls the suitable agent based on the user input and role as well as functionality of given sub agents.",
    sub_agents=[agent1, agent2, agent3, agent4]
)


