import Objs

class Device_handler:
    def __init__(self) -> None:
        self.hubs = []
        self.hosts = []
        self.time = 0

    def create_pc(self, name):
        return Objs.Computer(name)

    def create_hub(self, name, id):
        return Objs.Hub(name, id)

    def identify_connection_device(self, device1, device2):
        tokens = device1.split('_')

    def connect_pc_pc(self, pc_1 : Objs.Computer, pc_2 : Objs.Computer):
        if pc_1.connections[0] != None or pc_2.connections[0] != None:
            return False

        pc_1.connections.append(pc_2)
        pc_2.connections.append(pc_1)
        return True

    def connect_hub_hub(self, hub_1 : Objs.Hub, hub_2 : Objs.Hub,port_hub_1 : int, port_hub_2 : int):
        if hub_1[port_hub_1] != None or hub_2[port_hub_2] != None:
            return False

        hub_1.connections[port_hub_1] = hub_2
        hub_2.connections[port_hub_2] = hub_1  
        return True
    
    def connect_hub_pc(self, hub : Objs.Hub, pc : Objs.Computer, hub_port : int):
        if hub.connections[hub_port] != None or pc.connections[0] != None:
            return False

        hub.connections[hub_port] = pc
        pc.connections[0] = hub
        return True

    def disconnect_pc(self, pc : Objs.Computer):
        pc.connections[0] = None


    def disconnect_hub(self, hub : Objs.Hub, hub_port : int):
        hub.connections[hub_port] = None

    def send(self, origin_pc : Objs.Computer, info):
        pass