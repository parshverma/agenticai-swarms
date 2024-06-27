import os
from dotenv import load_dotenv
from swarms import BaseSwarm, Agent, OpenAIChat, AutoSwarmRouter

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Define the SalesSwarm class
class SalesSwarm(BaseSwarm):
    def __init__(self, name="sales_swarm", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

        # Define and add your agents here
        self.customer_data_analyzer = Agent(
            agent_name="Customer Data Analyzer",
            system_prompt="Analyze customer data to identify potential leads.",
            llm=OpenAIChat(openai_api_key=api_key),
            max_loops=1,
            autosave=True,
            dashboard=False,
            streaming_on=True,
            verbose=True,
            stopping_token="<DONE>",
        )
        self.pitch_generator = Agent(
            agent_name="Pitch Generator",
            system_prompt="Generate a sales pitch based on the analyzed customer data.",
            llm=OpenAIChat(openai_api_key=api_key),
            max_loops=1,
            autosave=True,
            dashboard=False,
            streaming_on=True,
            verbose=True,
            stopping_token="<DONE>",
        )
        self.revenue_forecaster = Agent(
            agent_name="Revenue Forecaster",
            system_prompt="Forecast potential revenue based on the sales pitch and customer data.",
            llm=OpenAIChat(openai_api_key=api_key),
            max_loops=1,
            autosave=True,
            dashboard=False,
            streaming_on=True,
            verbose=True,
            stopping_token="<DONE>",
        )

    def run(self, task: str, *args, **kwargs):
        # Add your multi-agent logic here
        analyzed_data = self.customer_data_analyzer.run(task, *args, **kwargs)
        pitch = self.pitch_generator.run(task, analyzed_data, *args, **kwargs)
        forecast = self.revenue_forecaster.run(task, pitch, analyzed_data, *args, **kwargs)
        return forecast

# Initialize the sales swarm instance
sales_swarm_instance = SalesSwarm()

# Create the AutoSwarmRouter with the sales swarm instance
router = AutoSwarmRouter(swarms=[sales_swarm_instance])

# Example of running the swarm
if __name__ == "__main__":
    task = "Analyze customer data and generate a sales pitch"
    result = sales_swarm_instance.run(task)
    print("Sales Swarm Result:", result)

# import os
# from swarms import BaseSwarm, Agent, AutoSwarm, AutoSwarmRouter, OpenAIChat

# # Define the SalesSwarm class
# class SalesSwarm(BaseSwarm):
#     def __init__(self, name="SalesSwarm", *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
        
#         # Define and add agents
#         self.customer_data_analyzer = Agent(
#             agent_name="Customer Data Analyzer",
#             system_prompt="Analyze customer data to identify opportunities.",
#             llm=OpenAIChat(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo"),
#             max_loops=1,
#             output_type=str,
#             metadata="json",
#             function_calling_format_type="OpenAI",
#             function_calling_type="json",
#             streaming_on=True,
#         )
        
#         self.pitch_generator = Agent(
#             agent_name="Pitch Generator",
#             system_prompt="Generate personalized sales pitches based on customer data.",
#             llm=OpenAIChat(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo"),
#             max_loops=1,
#             output_type=str,
#             metadata="json",
#             function_calling_format_type="OpenAI",
#             function_calling_type="json",
#             streaming_on=True,
#         )
        
#         self.revenue_forecaster = Agent(
#             agent_name="Revenue Forecaster",
#             system_prompt="Forecast revenue based on sales pitches and customer data.",
#             llm=OpenAIChat(openai_api_key=os.getenv("OPENAI_API_KEY"), model_name="gpt-3.5-turbo"),
#             max_loops=1,
#             output_type=str,
#             metadata="json",
#             function_calling_format_type="OpenAI",
#             function_calling_type="json",
#             streaming_on=True,
#         )
        
#         # Add agents to the swarm
#         self.add_agent(self.customer_data_analyzer)
#         self.add_agent(self.pitch_generator)
#         self.add_agent(self.revenue_forecaster)

#     def run(self, task: str, *args, **kwargs):
#         # Analyze customer data
#         analyzed_data = self.customer_data_analyzer.run(task, *args, **kwargs)
#         # Generate personalized sales pitch
#         pitch = self.pitch_generator.run(analyzed_data, *args, **kwargs)
#         # Forecast revenue based on pitch and customer data
#         revenue_forecast = self.revenue_forecaster.run(pitch, *args, **kwargs)
#         return revenue_forecast

# # Initialize the AutoSwarmRouter with SalesSwarm
# router = AutoSwarmRouter(swarms=[SalesSwarm])

# # Initialize AutoSwarm with the router
# autoswarm = AutoSwarm(
#     name="SalesSwarm",
#     description="A simple API to build and run swarms",
#     verbose=True,
#     router=router,
# )

# # Run the swarm with a task and save the output to a file
# if __name__ == "__main__":
#     task = "Analyze this customer data to identify opportunities and forecast revenue."
#     output = autoswarm.run(task)
    
#     # Save the output to a file
#     with open("swarm_output.txt", "w") as file:
#         file.write(output)

#     print("Output saved to swarm_output.txt")

# import os
# from swarms import BaseSwarm, Agent, OpenAIChat

# class SalesSwarm(BaseSwarm):
#     def __init__(self, name="kyegomez/salesswarm", *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
        
#         # Define and add agents
#         self.customer_data_analyzer = Agent(
#             agent_name="Customer Data Analyzer",
#             system_prompt="Analyze customer data to identify opportunities.",
#             llm=OpenAIChat(openai_api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo"),
#             max_loops=1,
#             autosave=True,
#             dashboard=False,
#             streaming_on=True,
#             verbose=True,
#             stopping_token="<DONE>",
#         )
#         self.add_agent(self.customer_data_analyzer)
        
#         self.pitch_generator = Agent(
#             agent_name="Pitch Generator",
#             system_prompt="Generate personalized sales pitches based on customer data.",
#             llm=OpenAIChat(openai_api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo"),
#             max_loops=1,
#             autosave=True,
#             dashboard=False,
#             streaming_on=True,
#             verbose=True,
#             stopping_token="<DONE>",
#         )
#         self.add_agent(self.pitch_generator)
        
#         self.revenue_forecaster = Agent(
#             agent_name="Revenue Forecaster",
#             system_prompt="Forecast revenue based on sales pitches and customer data.",
#             llm=OpenAIChat(openai_api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo"),
#             max_loops=1,
#             autosave=True,
#             dashboard=False,
#             streaming_on=True,
#             verbose=True,
#             stopping_token="<DONE>",
#         )
#         self.add_agent(self.revenue_forecaster)
    
#     def run(self, task: str, *args, **kwargs):
#         # Analyze customer data
#         analyzed_data = self.customer_data_analyzer.run(task, *args, **kwargs)
#         # Generate personalized sales pitch
#         pitch = self.pitch_generator.run(analyzed_data, *args, **kwargs)
#         # Forecast revenue based on pitch and customer data
#         revenue_forecast = self.revenue_forecaster.run(pitch, *args, **kwargs)
#         return revenue_forecast

# # Define and initialize the sales swarm
# sales_swarm = SalesSwarm()

# # Run a task using the sales swarm
# result = sales_swarm.run("Analyze customer data and generate a sales forecast")
# print(result)

# # Save the result to a file
# with open("sales_result.txt", "w") as file:
#     file.write(result)






import os
from dotenv import load_dotenv

# Import the OpenAIChat model and the Agent struct
from swarms import Agent, OpenAIChat, SwarmNetwork

# Load the environment variables
load_dotenv()

# Get the API key from the environment
api_key = os.environ.get("OPENAI_API_KEY")
print("Got API Key")
# Initialize the language model
llm = OpenAIChat(
    temperature=0.5,
    openai_api_key=api_key,
    model="gpt-3.5-turbo"
)

print("Initialized llm")

## Initialize the workflow
agent = Agent(llm=llm, max_loops=1, agent_name="Social Media Manager")
agent2 = Agent(llm=llm, max_loops=1, agent_name="Product Manager")
agent3 = Agent(llm=llm, max_loops=1, agent_name="SEO Manager")
print("Initialized agents")




# Load the swarmnet with the agents
swarmnet = SwarmNetwork(
    agents=[agent, agent2, agent3],
)

print("Loaded swarmnet")


# List the agents in the swarm network
out = swarmnet.list_agents()
print(out)

# Run the workflow on a task
single_agent_output = swarmnet.run_single_agent(
    agent2.id, "Generate a 10,000 word blog on health and wellness."
)
print(single_agent_output)

# Run all the agents in the swarm network on a task
many_agents_output = swarmnet.run_many_agents("Generate a 10,000 word blog on health and wellness.")
print(many_agents_output)

# Save the results to a file
with open("swarm_output.txt", "w") as file:
    file.write("Single Agent Output:\n")
    file.write(single_agent_output)
    file.write("\n\nMany Agents Output:\n")
    file.write(many_agents_output)

print("Output saved to swarm_output.txt")
