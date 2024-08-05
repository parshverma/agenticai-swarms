import os
from swarms import OpenAIChat, Agent, SequentialWorkflow
from dotenv import load_dotenv

load_dotenv()

# Load the environment variables
api_key = os.getenv("OPENAI_API_KEY")


# Initialize the language agent
llm = OpenAIChat(
    temperature=0.5,
    model_name="gpt-3.5-turbo",
    openai_api_key=api_key,
    max_tokens=4000,
)

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



# # Initialize the agent with the language agent
# agent1 = Agent(llm=llm, max_loops=1)

# # Create another agent for a different task
# agent2 = Agent(llm=llm, max_loops=1)

# # Create another agent for a different task
# agent3 = Agent(llm=llm, max_loops=1)

# # Create the workflow
# workflow = SequentialWorkflow(max_loops=1, agents=[agent1, agent2, agent3])

# # Add tasks to the workflow
# workflow.add(
#     agent1,
#     "Generate a 10,000 word blog on health and wellness.",
# )

# # Suppose the next task takes the output of the first task as input
# workflow.add(
#     agent2,
#     "Summarize the generated blog",
# )

# # Run the workflow
# workflow.run()

# # Output the results
# for task in workflow.tasks:
#     print(f"Task: {task.description}, Result: {task.result}")

