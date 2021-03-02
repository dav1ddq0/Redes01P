import Objs

class Instructions:
    @staticmethod
    def create_pc(name):
        return Objs.Computer(name)

    @staticmethod
    def create_hub(name, id):
        return Objs.Hub(name, id)

    @staticmethod
    def connect_pc_pc(pc_1 : Objs.Computer, pc_2 : Objs.Computer):
        if pc_1.connections[0] != None or pc_2.connections[0] != None:
            return False

        pc_1.connections.append(pc_2)
        pc_2.connections.append(pc_1)
        return True

    @staticmethod
    def connect_hub_hub(hub_1 : Objs.Hub, hub_2 : Objs.Hub,port_hub_1 : int, port_hub_2 : int):
        if hub_1[port_hub_1] != None or hub_2[port_hub_2] != None:
            return False

        hub_1.connections[port_hub_1] = hub_2
        hub_2.connections[port_hub_2] = hub_1  
        return True
    
    @staticmethod
    def connect_hub_pc(hub : Objs.Hub, pc : Objs.Computer, hub_port : int):
        if hub.connections[hub_port] != None or pc.connections[0] != None:
            return False

        hub.connections[hub_port] = pc
        pc.connections[0] = hub
        return True

    @staticmethod
    def disconnect_pc(pc : Objs.Computer):
        pc.connections[0] = None

    @staticmethod
    def disconnect_hub(hub : Objs.Hub, hub_port : int):
        hub.connections[hub_port] = None

    @staticmethod
    def send(origin_pc : Objs.Computer, info):
        pass