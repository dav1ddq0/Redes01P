class Computer:
    def __init__(self, name) -> None:
        self.name = name
        self.connections = [None]*1

class Hub:
    def __init__(self, name, ports_amount : int) -> None:
        self.name = name
        self.connections = [None]*ports_amount