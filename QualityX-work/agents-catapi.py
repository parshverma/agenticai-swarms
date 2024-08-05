import os
import time
import requests
from swarms import OpenAIChat, Agent, SequentialWorkflow, tool
from dotenv import load_dotenv

load_dotenv()

# Load the environment variables
api_key = os.getenv("OPENAI_API_KEY")

@tool
def fetch_cat_fact() -> str:
    """
    Fetch a random cat fact from the API.
    
    Args:
         None

    Returns:
        str: A random cat fact.
    """
    response = requests.get("https://catfact.ninja/fact")
    fact = response.json().get("fact")
    print(fact)
    return fact


# def analyze_cat_fact(fact: str) -> str:
#     """
#     Analyze the given cat fact.

#     Args:
#         fact (str): The cat fact to analyze.

#     Returns:
#         str: The analysis of the cat fact.
#     """
#     return f"Analysis: This cat fact is quite interesting. It tells us that '{fact}'. Such facts can be great conversation starters!"

# Initialize the language model
llm = OpenAIChat(
    temperature=0.5,
    model_name="gpt-3.5-turbo",
    openai_api_key=api_key,
    max_tokens=4000,
    
)


agent1 = Agent(
    agent_name="CatFactFetcher",
    system_prompt="Fetch a random cat fact",
    llm=llm,
    max_loops=1,
    dashboard=False,
    tools=[fetch_cat_fact],
)


agent2 = Agent(
    agent_name="CatFactAnalyzer",
    system_prompt="Analyze the given cat fact",
    llm=llm,
    max_loops=1,
    dashboard=False,
)

# Create the Sequential workflow
workflow = SequentialWorkflow(
    agents=[agent1], max_loops=1, verbose=False
)

# Run the workflow with a delay
print("Starting workflow with task: Fetch a random cat fact and then analyze it.")
workflow.run("Fetch a random cat fact and analyze the given cat fact")

# Add delay to ensure the cat fact is fetched before passing to the next agent
time.sleep(2)

# Fetch the cat fact
# cat_fact = fetch_cat_fact()
# print(f"Fetched Cat Fact: {cat_fact}")

# Analyze the fetched cat fact
# analysis_result = analyze_cat_fact(cat_fact)
# print(f"Analysis Result: {analysis_result}")

# Print the final results
# print(f"Cat Fact: {cat_fact}")
# print(f"Analysis: {analysis_result}")
