from sales_swarm.sales_swarm import autoswarm

# Define a task to run the swarm
task = "Analyze the customer data and generate insights."

# Run the swarm on the task
result = autoswarm.run(task)
print("Swarm result:", result)
