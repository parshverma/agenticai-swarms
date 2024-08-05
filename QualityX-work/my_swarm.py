# from swarms.models import HuggingfaceLLM
# from swarms import AutoSwarm, AutoSwarmRouter, BaseSwarm, Agent
# import torch

# # Define the HuggingfaceLLM for each agent
# def create_huggingface_llm_agent(agent_name, system_prompt):
#     inference = HuggingfaceLLM(
#         model_id="gpt2",
#         quantize=False,
#         verbose=True,
#     )

#     device = "cuda" if torch.cuda.is_available() else "cpu"
#     inference.model.to(device)

#     return Agent(
#         agent_name=agent_name,
#         system_prompt=system_prompt,
#         llm=inference,
#         max_loops=1,
#         autosave=True,
#         dashboard=False,
#         streaming_on=True,
#         verbose=True,
#         stopping_token="<DONE>",
#     )

# # Define and create agents
# customer_data_analyzer = create_huggingface_llm_agent(
#     agent_name="Customer Data Analyzer",
#     system_prompt="Analyze customer data to identify opportunities.",
# )

# pitch_generator = create_huggingface_llm_agent(
#     agent_name="Pitch Generator",
#     system_prompt="Generate personalized sales pitches based on customer data.",
# )

# revenue_forecaster = create_huggingface_llm_agent(
#     agent_name="Revenue Forecaster",
#     system_prompt="Forecast revenue based on sales pitches and customer data.",
# )

# class MySwarm(BaseSwarm):
#     def __init__(self, name="my_gpt2_swarm", *args, **kwargs):
#         agents = [customer_data_analyzer, pitch_generator, revenue_forecaster]
#         super(MySwarm, self).__init__(agents=agents, *args, **kwargs)
#         self.name = name

#     def run(self, task: str, *args, **kwargs):
#         # Analyze customer data
#         analyzed_data = self.agents[0].run(task, *args, **kwargs)
#         # Generate personalized sales pitch
#         pitch = self.agents[1].run(analyzed_data, *args, **kwargs)
#         # Forecast revenue based on pitch and customer data
#         revenue_forecast = self.agents[2].run(pitch, *args, **kwargs)
#         return revenue_forecast

# # Instantiate the swarm with agents
# my_swarm_instance = MySwarm()

# # Ensure the agents are passed correctly to the router
# router = AutoSwarmRouter(swarms=[my_swarm_instance], agents=[customer_data_analyzer, pitch_generator, revenue_forecaster])

# # Initialize AutoSwarm with the router
# autoswarm = AutoSwarm(
#     name="my_gpt2_swarm",
#     description="A simple API to build and run swarms",
#     verbose=True,
#     router=router,
# )

# # Run the swarm
# result = autoswarm.run("Analyze these financial data and give me a summary")
# print(result)

import os
from swarms.models import HuggingfaceLLM
from swarms import BaseSwarm, Agent, AutoSwarm, AutoSwarmRouter
import torch

# Define the HuggingfaceLLM for each agent
def create_huggingface_llm_agent(agent_name, system_prompt):
    inference = HuggingfaceLLM(
        model_id="gpt2",
        quantize=False,
        verbose=True,
    )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    inference.model.to(device)

    return Agent(
        agent_name=agent_name,
        system_prompt=system_prompt,
        llm=inference,
        max_loops=1,
        output_type=str,
        metadata="json",
        function_calling_format_type="OpenAI",
        function_calling_type="json",
        streaming_on=True,
    )

# Purpose = To detect email spam using three different agents
spam_detector_1 = create_huggingface_llm_agent(
    agent_name="SpamDetector1",
    system_prompt="Detect if the email is spam or not, and provide your reasoning",
)

spam_detector_2 = create_huggingface_llm_agent(
    agent_name="SpamDetector2",
    system_prompt="Detect if the email is spam or not, and provide your reasoning",
)

spam_detector_3 = create_huggingface_llm_agent(
    agent_name="SpamDetector3",
    system_prompt="Detect if the email is spam or not, and provide your reasoning",
)

# Define the Swarm class
class SpamDetectionSwarm(BaseSwarm):
    def __init__(self, name="spam_detection_swarm", agents=None, *args, **kwargs):
        if agents is None:
            agents = []
        super(SpamDetectionSwarm, self).__init__(agents=agents, *args, **kwargs)
        self.name = name

    def run(self, task: str, *args, **kwargs):
        # Initial task input for the first agent
        data = task
        for agent in self.agents:
            data = agent.run(data, *args, **kwargs)
            print(f"Output from {agent.agent_name}: {data}")

        return data

# Instantiate the swarm with agents
spam_detection_swarm_instance = SpamDetectionSwarm(agents=[spam_detector_1, spam_detector_2, spam_detector_3])

# Ensure the agents are passed correctly to the router
router = AutoSwarmRouter(swarms=[spam_detection_swarm_instance], custom_params=None, agents=[spam_detector_1, spam_detector_2, spam_detector_3])

# Initialize AutoSwarm with the router
autoswarm = AutoSwarm(
    name="spam_detection_swarm",
    description="A simple API to build and run swarms",
    verbose=True,
    router=router,
)

# Run the swarm with a task
result = autoswarm.run("Find YSL bag with the biggest discount")
print(f"Final result: {result}")
