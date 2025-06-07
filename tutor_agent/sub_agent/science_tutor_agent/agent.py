from google.adk.agents import Agent

from .tools import get_constants

science_tutor_agent = Agent(
    name="science_tutor_agent",
    model="gemini-2.0-flash",
    description="An agent that helps users with science-related questions and problems.",
    instruction="""You are a helpful science tutor. 
        You can answer questions related to various fields of science, 
        including physics, chemistry, biology, and earth science. 
        If the user asks scientific constants then use get_constants() to fetch the constants from a dictionary.
        If the user asks a question that is not related to science, you should redirect to the tutor agent.
        """,
    tools=[get_constants],
)
