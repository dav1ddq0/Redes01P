class Computer:
    def __init__(self, id : int) -> None:
        self.name = f"PC_{id}"
        self.connections = []

class Hub:
    def __init__(self, id : int) -> None:
        self.name = f"Hub_{id}"
        self.connections = []