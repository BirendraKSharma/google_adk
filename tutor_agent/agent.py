from google.adk.agents import Agent

from .sub_agent.math_tutor_agent.agent import math_tutor_agent
from .sub_agent.science_tutor_agent.agent import science_tutor_agent


root_agent = Agent(
    name="tutor_agent",
    model="gemini-2.0-flash",
    description="An agent that helps users with their questions and tasks.",
    instruction="""
    You are a helpful assistant that can use the following tools:
    
    Always delegate tasks to the appropriate sub-agent based on the user's request and on your knowledge.


    You have access to the following sub-agents:
    - math_tutor_agent: An agent that helps users with math problems by performing basic arithmetic operations.
    - science_tutor_agent: An agent that helps users with science-related questions and problems.
    """,

    sub_agents=[math_tutor_agent, science_tutor_agent]
)
    