
import os
from swarms import OpenAIChat, Agent, SequentialWorkflow
from dotenv import load_dotenv

api_key = os.getenv("OPENAI_API_KEY")
print(api_key)
# Initialize the language model agent (e.g., GPT-3)
"""
llm = OpenAIChat(
    temperature=0.5,
    model_name="gpt-3.5-turbo",
    openai_api_key=api_key,
    max_tokens=800,)

# Initialize agents for individual tasks
agent1 = Agent(
    agent_name="Blog generator",
    system_prompt="Generate a blog post like stephen king",
    llm=llm,
    max_loops=1,
    dashboard=False,
    tools=[],
)
agent2 = Agent(
    agent_name="summarizer",
    system_prompt="Sumamrize the blog post",
    llm=llm,
    max_loops=1,
    dashboard=False,
    tools=[],
)

# Create the Sequential workflow
workflow = SequentialWorkflow(
    agents=[agent1, agent2], max_loops=1, verbose=False
)

# Run the workflow
workflow.run(
    "Generate a blog post on how swarms of agents can help businesses grow."
)
"""