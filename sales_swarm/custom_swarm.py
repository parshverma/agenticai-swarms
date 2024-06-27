from swarms import AutoSwarmRouter, AutoSwarm

class CustomAutoSwarmRouter(AutoSwarmRouter):
    def __init__(self, *args, **kwargs):
        print(f"Initializing CustomAutoSwarmRouter with args: {args}, kwargs: {kwargs}")
        super().__init__(*args, **kwargs)
        print(f"CustomAutoSwarmRouter initialized with swarms: {self.swarms}")

class CustomAutoSwarm(AutoSwarm):
    def __init__(self, *args, **kwargs):
        print(f"Initializing CustomAutoSwarm with args: {args}, kwargs: {kwargs}")
        super().__init__(*args, **kwargs)
        print(f"CustomAutoSwarm initialized with router: {self.router}")
