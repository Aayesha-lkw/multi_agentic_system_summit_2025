import logging
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from multi_agent.base_agent import root_agent


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

APP_NAME = "app_name1"
USER_ID = "user_id1"
SESSION_ID = "session_id1"
session_service = InMemorySessionService()
root_agent_seq = root_agent
runner = Runner(app_name=APP_NAME, agent=root_agent_seq, session_service=session_service)
chat_history = []

async def initialize_session():
    existing_session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    if not existing_session:
        await session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=SESSION_ID
        )

async def process_input(user_text: str) -> str:
    try:
        await initialize_session()
        current_session = await session_service.get_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
        if not current_session:
            logger.error("Session not found!")
            return
        content = types.Content(role='user', parts=[types.Part(text=user_text)])
        async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
            if event.is_final_response() and event.content and event.content.parts:
                response_text = event.content.parts[0].text
        chat_history.append({"role": "User", "message": user_text})
        chat_history.append({"role": "Bot", "message": response_text})
        return response_text
    except Exception as e:
        print(f"Error: {e}")

def get_history():
    return chat_history



