import Objs

class Device_handler:
    @property
    def hosts(self):
        return self.hosts

    def __init__(self) -> None:
        self.hubs = []
        self.hosts = []
        self.connections = {}
        self.time = 0

    def __validate_send(self, name_port):
        for host in self.hosts:
            if host.name + "_1" == name_port:
                return True

        return False

    def __validate_disconnection(self, name_port):
        _, port = name_port.split('_')
        for host in self.hosts:
            if host.name + "_1" == name_port and name_port in self.connections.keys() and self.connections[name_port] != None :
                return 1

        for hub in self.hubs:
            if hub.name + "_{}".format(port) == name_port and name_port in self.connections.keys() and self.connections[name_port] != None:
                return 1

        return 0
    
    def __validate_connection(self, name_port): #Private method to identify wether a device is a hub or a host
        _, port = name_port.split('_')
        for host in self.hosts:
            if host.name + "_1" == name_port and self.connections[name_port] == None or name_port not in self.connections.keys():
                return 1, host, 2

        for hub in self.hubs:
            if hub.name + "_{}".format(port) == name_port and self.connections[name_port] == None or name_port not in self.connections.keys():
                return 1, hub, 1

        return 0, None
        
    def create_pc(self, name):
        newpc=Objs.Computer(name)
        self.hosts.append(newpc)

    def create_hub(self, name, ports):
        newhub = Objs.Hub(name, ports)
        self.hubs.append(newhub)

    def setup_connection(self, name_port1, name_port2):
        #0 not_setted #1 => Hub #2 => PC
        _,port1 = name_port1.split('_')
        _,port2 = name_port2.split('_')
        port1 = int(port1); port2  = int(port2)
        valid_ports = False #This value wil be used to notify if it was posible to stablish the desired connection between the devices
        device1 = None; device2 = None
        device1_Type = 0; device2_Type = 0
        #device1_type = 0; device2_type = 0 #Initially i assume the devices haven't been created i.e. do not exist in either hubs or hosts lists

        valid_ports, device1 = self.__validate_connection(name_port1)
        valid_ports, device2 = self.__validate_connection(name_port2)

        if(valid_ports):
            if device1_Type == 1 and device2_Type == 1:
                self.connections[name_port1] = device2.ports[port2]
                self.connections[name_port2] = device1.ports[port1]
            
            elif device1_Type == 1 and device2_Type == 2:
                self.connections[name_port1] = device2.port
                self.connections[name_port2] = device1.ports[port1]
            
            elif device1_Type == 2 and device2_Type == 1:
                self.connections[name_port1] = device2.port[port2]
                self.connections[name_port2] = device1.port

            elif device1_Type == 2 and device2_Type == 2:
                self.connections[name_port1] = device2.port
                self.connections[name_port2] = device1.port
            

        #if device1_type == 1 and device2_type == 1:
        #    conection_stablished = self.__connect_hub_hub(device1,device2,device1_port,device2_port)
                #
        #elif device1_type == 1 and device2_type == 2:
        #    conection_stablished = self.__connect_hub_pc(device1,device2,device1_port)
        #
        #elif device1_type == 2 and device1_type == 1:
        #    conection_stablished = self.__connect_hub_pc(device2,device1,device2_port)
        #
        #elif device1_type == 2 and device1_type == 2: 
        #    conection_stablished = self.__connect_pc_pc(device1,device2)
    
        return valid_ports 

    def __connect_pc_pc(self, pc_1 : Objs.Computer, pc_2 : Objs.Computer):
        if pc_1.connections[0] != None or pc_2.connections[0] != None:
            return False

        pc_1.connections.append(pc_2)
        pc_2.connections.append(pc_1)
        return True
    
    #def connect(por1:str,port2:str):
    #    if port1 not in Objs.ports.keys():
    #        print(f"Error the port {port1} not exist")
    #    elif port2 not in Objs.ports.keys():
    #        print(f"Error the port {port2} not exist")
    #    else:
    #        Objs.ports[port1].connect(por2)

    def __connect_hub_hub(self, hub_1 : Objs.Hub, hub_2 : Objs.Hub,port_hub_1 : int, port_hub_2 : int):
        if hub_1[port_hub_1] != None or hub_2[port_hub_2] != None:
            return False

        hub_2.connections[port_hub_2] = hub_1  
        hub_1.connections[port_hub_1] = hub_2
        return True

    def __connect_hub_pc(self, hub : Objs.Hub, pc : Objs.Computer, hub_port : int):
        if hub.connections[hub_port] != None or pc.connections[0] != None:
            return False
        hub.connections[hub_port] = pc
        pc.connections[0] = hub
        return True

    def shutdown_connection(self, name_port):
        valid_port = False
        valid_port = self.__validate_disconnection(name_port)

        if(valid_port):
            self.connections[name_port] = None

        return valid_port

    #def disconnect(self, port):
    #    if port not in Objs.ports.keys():
    #        print(f"This port {port} not exist")
    #    else:
    #        Objs.ports[port].disconnect()

            
    # def __disconnect_pc(self, pc : Objs.Computer):
    #     if pc.connections[0] != None:
    #         pc.connections[0] = None
    #         return True
        
    #     return False

    # def __disconnect_hub(self, hub : Objs.Hub, hub_port : int):
    #     if hub.connections[hub_port] != None:
    #         hub.connections[hub_port] = None
    #         return True

    #     return False

    def send(self, origin_pc : Objs.Computer, info):
        if self.__validate_send(origin_pc):
            pass

        else : print("Wether the device is not a host, or the host currently doesnt exist")   
        