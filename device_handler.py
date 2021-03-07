import Objs

errors = {  1 : "is busy",
            2 : "does not exist",
            3 : "is free"
        }
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
        error_type = 0; device = None
        _, port = name_port.split('_')
        for host in self.hosts:
            if host.name + "_1" == name_port:
                if name_port in self.connections.keys() and self.connections[name_port] != None:
                    if(host.port.status == Objs.Status.Null):
                        device = host
                    else : error_type = 5
                else : error_type = 
                    
        if(device == None):
            for hub in self.hubs:
                if hub.name + "_{}".format(port) == name_port:
                    device = hub, error_type = 4
        
        if(device == None):
            error_type = 2

        return error_type, device

    def __validate_disconnection(self, name_port):
        if name_port not in ports:
             print(f"port {name_port} {errors[2]}")
             return False
        elif name_port not in connections:
                print(f"port {name_port} {errors[3]}")
                return False
        return True        
    
    def __validate_connection(self, name_port1,name_port2): #Private method to identify wether a device is a hub or a host
        if name_port1 not in ports_d.keys():
            print(f"port {name_port1} {errors[2]}")
            return False
        elif name_port2 not in ports_d.keys():
            print(f"port {name_port2} {errors[2]}")
            return False
        else:
            port1=ports_d[name_port1]
            port2=ports_d[name_port2]
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

        if __validate_connection(name_port1,name_port2):
            port1=ports_d(name_port1)
            port2=ports_d(name_port2)
            connections[name_port1]=name_port2
            connections[name_port2]=name_port1
            port1.cable_connected=True
            porr2.cable_connected=False
        

    
    def shutdown_connection(self, name_port):
        if __validate_disconnection(name_port):
            port1 =ports_d[nameport]
            port1.cable_connected=False
            nameport2=connections[name_port]
            del connections[name_port]
            del connections[name_port2]
            
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

    
    def send(self, origin_pc, data):
        #error_type 3 => the port is not connected
        #error_type 4 => the device must be a host
        #error_type 5 => the host is busy (Collision)
        
        device = None; error_type = 0
        device, error_type = self.__validate_send(origin_pc)

        if(error_type == 0): #El send es valido
            device.port.status = Objs.Status.Zero if data == '0' else Objs.Status.One
            destination_device, destination_port = self.connections[origin_pc]
            self.__spread_data(device, data)   

    
    def __spread_data(self, origin, data, origin_port = None):
        
        if isinstance(origin, Objs.Computer):
            origin.port.status = Objs.Status.Zero if data == '0' else Objs.Status.One
           
            self.__spread_data(device, data, destiny_port)


        else :
            

      