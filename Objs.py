import os
class Computer:
    def __init__(self, name) -> None:
        self.name = name
        self.connections = [None]*1
        self.file=open(f"{name}.txt",'w')

class Hub:
    def __init__(self, name, ports_amount : int) -> None:
        self.name = name
        self.connections = [None]*ports_amount
        self.file=open(f"{name}.txt",'w')