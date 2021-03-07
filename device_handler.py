import Objs

errors = {1: "is busy", 2: "does not exist", 3: "is free"}


class Device_handler:
    @property
    def hosts(self):
        return self.hosts

    def __init__(self) -> None:
        self.hubs = []
        self.hosts = []
        self.connections = {}
        self.ports={}
        self.time = 0

    def __validate_send(self, name_port):
        for host in self.hosts:
            if host.name + "_1" == name_port:
                return True

        return False

    def __validate_disconnection(self, name_port):
        if name_port not in Objs.ports:
             print(f"port {name_port} {errors[2]}")
             return False
        elif name_port not in self.connections:
                print(f"port {name_port} {errors[3]}")
                return False
        return True        
    
    def __validate_connection(self, name_port1,name_port2): #Private method to identify wether a device is a hub or a host
        if name_port1 not in Objs.ports_d.keys():
            print(f"port {name_port1} {errors[2]}")
            return False
        elif name_port2 not in Objs.ports_d.keys():
            print(f"port {name_port2} {errors[2]}")
            return False
        else:
            port1= Objs.ports_d[name_port1]
            port2= Objs.ports_d[name_port2]
            if  port1.cable_connected:
                print(f"Port{name_port1} {errors[1]}")
                return False
            elif port2.cable_connected:    
                print(f"Port{name_port2} {errors[1]}")
                return False
        return True
            

        
    def create_pc(self, name):
        newpc =Objs.Computer(name)
        self.hosts.append(newpc)

    def create_hub(self, name, ports):
        newhub = Objs.Hub(name, ports)
        self.hubs.append(newhub)

    def setup_connection(self, name_port1, name_port2):

        if self.__validate_connection(name_port1, name_port2):
            port1 = Objs.ports_d(name_port1)
            port2 = Objs.ports_d(name_port2)
            self.connections[name_port1] = name_port2
            self.connections[name_port2] = name_port1
            port1.cable_connected = True
            port2.cable_connected = False
        

    
    def shutdown_connection(self, name_port):
        if self.__validate_disconnection(name_port):
            port1 = Objs.ports_d[name_port]
            port1.cable_connected = False
            name_port2 = self.connections[name_port]
            del self.connections[name_port]
            del self.connections[name_port2]


    
    def send(self, origin_pc : Objs.Computer, info):
        pass
        # if self.__validate_send(origin_pc):
        #     pass
        #
        # else : print("Wether the device is not a host, or the host currently doesnt exist")
        