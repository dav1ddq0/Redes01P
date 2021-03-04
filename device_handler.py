import Objs

class Device_handler:
    @property
    def host(self):
        return self.host
    def __init__(self) -> None:
        self.hubs = []
        self.hosts = []
        self.time = 0

    def __identify_device(self, name): #Private method to identify wether a device is a hub or a host
        for host in self.hosts:
            if host.name == name:
                return 2, host

        for hub in self.hubs:
            if hub.name == name:
                return 1, hub

        return 0, None
        
    def create_pc(self, name):
        newpc=Objs.Computer(name)
        hosts.append(newpc)

    def create_hub(self, name, ports):
        newhub = Objs.Hub(name, ports)
        hubs.append(newhub)

    def setup_device_connection(self, device1_name, device2_name, device1_port, device2_port):
        #0 not_setted #1 => Hub #2 => PC 
        conection_stablished = False #This value wil be used to notify if it was posible to stablish the desired connection between the devices
        device1_type = 0; device2_type = 0 #Initially i assume the devices haven't been created i.e. do not exist in either hubs or hosts lists

        device1_type, device1 = self.__identify_device(device1_name)
        device2_type, device2 = self.__identify_device(device2_name)

        if device1_type == 1 and device2_type == 1:
            conection_stablished = self.__connect_hub_hub(device1,device2,device1_port,device2_port)

        elif device1_type == 1 and device2_type == 2:
            conection_stablished = self.__connect_hub_pc(device1,device2,device1_port)
        
        elif device1_type == 2 and device1_type == 1:
            conection_stablished = self.__connect_hub_pc(device2,device1,device2_port)

        elif device1_type == 2 and device1_type == 2: 
            conection_stablished = self.__connect_pc_pc(device1,device2)
    
        return conection_stablished 

    def __connect_pc_pc(self, pc_1 : Objs.Computer, pc_2 : Objs.Computer):
        if pc_1.connections[0] != None or pc_2.connections[0] != None:
            return False

        pc_1.connections.append(pc_2)
        pc_2.connections.append(pc_1)
        return True

    def __connect_hub_hub(self, hub_1 : Objs.Hub, hub_2 : Objs.Hub,port_hub_1 : int, port_hub_2 : int):
        if hub_1[port_hub_1] != None or hub_2[port_hub_2] != None:
            return False

        hub_1.connections[port_hub_1] = hub_2
        hub_2.connections[port_hub_2] = hub_1  
        return True
    
    def __connect_hub_pc(self, hub : Objs.Hub, pc : Objs.Computer, hub_port : int):
        if hub.connections[hub_port] != None or pc.connections[0] != None:
            return False

        hub.connections[hub_port] = pc
        pc.connections[0] = hub
        return True

    def shutdown_device_connection(self, device_name, device_port):
        device_type, device = self.__identify_device(device_name)
        connection_succesfully_shutdown = False
        if device_type == 1 : 
            connection_succesfully_shutdown = self.__disconnect_hub(device, device_port)
        elif device_type == 2 : 
            connection_succesfully_shutdown = self.__disconnect_pc(device)

        return connection_succesfully_shutdown

    def __disconnect_pc(self, pc : Objs.Computer):
        if pc.connections[0] != None:
            pc.connections[0] = None
            return True
        
        return False

    def __disconnect_hub(self, hub : Objs.Hub, hub_port : int):
        if hub.connections[hub_port] != None:
            hub.connections[hub_port] = None
            return True

        return False

    def send(self, origin_pc : Objs.Computer, info):
        pass