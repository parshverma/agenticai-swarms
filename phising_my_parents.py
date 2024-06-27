import os 
from swarms import OpenAIChat, Agent, AgentRearrange
import contextlib

# Purpose = To detect email spam using three different agents
agent1 = Agent(
    agent_name="SpamDetector1",
    system_prompt="Detect if the email is spam or not, and provide your reasoning",
    llm=OpenAIChat(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo"),
    max_loops=1,
    output_type=str,
    metadata="json",
    function_calling_format_type="OpenAI",
    function_calling_type="json",
    streaming_on=True,
)

agent2 = Agent(
    agent_name="SpamDetector2",
    system_prompt="Further analyze the following email content for spam indicators and provide detailed reasoning: {previous_output}",
    llm=OpenAIChat(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo"),
    max_loops=1,
    output_type=str,
    metadata="json",
    function_calling_format_type="OpenAI",
    function_calling_type="json",
    streaming_on=True,
)

agent3 = Agent(
    agent_name="SpamDetector3",
    system_prompt="Review the detailed reasoning provided and confirm if the email is spam, giving a final verdict with reasons: {previous_output}",
    llm=OpenAIChat(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo"),
    max_loops=1,
    output_type=str,
    metadata="json",
    function_calling_format_type="OpenAI",
    function_calling_type="json",
    streaming_on=True,
)

swarm = AgentRearrange(
    flow="SpamDetector1 -> SpamDetector2 -> SpamDetector3",
    agents=[agent1, agent2, agent3],
    logging_enabled=True,
    max_loops=1,
)

# Run all the agents and save the output to a file
with open('output3.txt', 'w') as f:
    with contextlib.redirect_stdout(f):
        input_task = "Review the following email and determine if it's spam: 'Get your free YSL bag now!'"
        print(f"Initial Task: {input_task}")
        result1 = agent1.run(input_task)
        print(f"Output from SpamDetector1: {result1}")
        
        result2 = agent2.run(result1)
        print(f"Output from SpamDetector2: {result2}")
        
        result3 = agent3.run(result2)
        print(f"Output from SpamDetector3: {result3}")
        
        print(f"Final Output: {result3}")
