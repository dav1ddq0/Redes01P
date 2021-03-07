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
        error_type = 0; device = None
        _, port = name_port.split('_')
        for host in self.hosts: #Busquemos name_port en hosts
            if host.name + "_1" == name_port: # Si es un host
                if name_port in self.connections.keys(): #Si ya esta en el diccionarion connections
                    if self.connections[name_port] != None: #Si esta ocupado el puerto
                        device = host #asignamos el dispositivo desconectar y terminamos
                        break
                    else : error_type = 3 #Si el puerto esta libre, error, no se puede desconectar, porque el puerto esta libre

                else : error_type = 3 #Si el puerto no esta en el diccionario connections, error, no se puede desconectar, porque el puerto esta libre

        if(device == None):#Si device no era un host
            for hub in self.hubs:#Veamos si es un hub
                if hub.name + "_{}".format(port) == name_port:#Si es un hub
                    if name_port in self.connections.keys(): #Si ya esta en el diccionarion connections
                        if self.connections[name_port] != None: #Si esta ocupado el puerto
                            device = hub #asignamos el dispositivo a desconectar y terminamos
                            break
                        else : error_type = 3 #Si el puerto esta libre, error, no se puede desconectar, porque el puerto esta libre

                    else : error_type = 3 #Si el puerto no esta en el diccionario connections, error, no se puede desconectar, porque el puerto esta libre

        if(device == None): #Si device no era un host ni un hub, entonces no existe
            error_type = 2 #Error el dispositivo no existe

        return error_type, device #retornamos el tipo de error y el dispositivo a desconectar
    
    def __validate_connection(self, name_port): #Private method to identify wether a device is a hub or a host
        error_type = 0; device = None; device_type = None
        _, port = name_port.split('_')
        for host in self.hosts:
            if host.name + "_1" == name_port: #Busquemos name_port en hosts
                if name_port not in self.connections.keys() or self.connections[name_port] == None: #Si no esta en el diccionario connections o esta pero su value es None
                    device, device_type = host, 2 #Podemos conectarlo, por tanto, asiganmos los valores de device y su tipo para usar cuando establezcamos la conexion
                    break

                else  : error_type = 1 #Esto quiere decir que name_port esta en el diccionario y su valor no es None, error, porque el puerto esta ocupado

        if(device == None): #Si device no era un host
            for hub in self.hubs: #Veamos si es un hub
                if hub.name + "_{}".format(port) == name_port: ##Si es un hub
                    if name_port not in self.connections.keys() or self.connections[name_port] == None: #Si no esta en el diccionario connections o esta pero su value es None
                        device, device_type = hub, 1 #Podemos conectarlo, por tanto, asignamos los valores de device y su tipo para usar cuando establezcamos la conexion
                        break

                    else : error_type = 1 #Esto quiere decir que name_port esta en el diccionario y su valor no es None, error, porque el puerto esta ocupado

        if(device == None): #Si device no era un host ni un hub, entonces no existe
            error_type = 2 #Error el dispositivo no existe

        return error_type, device, device_type #retornamos el tipo de error y el dispositivo a conectar

        
    def create_pc(self, name):
        newpc =Objs.Computer(name)
        self.hosts.append(newpc)

    def create_hub(self, name, ports):
        newhub = Objs.Hub(name, ports)
        self.hubs.append(newhub)

    def setup_connection(self, name_port1, name_port2):
        #error types : 0 => not an error, #1 => one of the ports is already connected #2 => one of the ports does not exist
        #device types : 0 => not a device, 1 => hub, 2 => host
        _,port1 = name_port1.split('_')
        _,port2 = name_port2.split('_')
        port1 = int(port1); port2  = int(port2)
        error_type_name_port1 = 0; error_type_name_port2 = 0
        device1 = None; device2 = None
        device1_Type = 0; device2_Type = 0

        error_type_name_port1, device1, device1_Type = self.__validate_connection(name_port1)
        error_type_name_port2, device2, device2_Type  = self.__validate_connection(name_port2)

        if(error_type_name_port1 == 0 and error_type_name_port2 == 0):
            if device1_Type == 1 and device2_Type == 1:
                self.connections[name_port1] = (device2, port2)
                self.connections[name_port2] = (device1, port1)
            
            elif device1_Type == 1 and device2_Type == 2:
                self.connections[name_port1] = device2
                self.connections[name_port2] = (device1, port1)
            
            elif device1_Type == 2 and device2_Type == 1:
                self.connections[name_port1] = (device2, port2)
                self.connections[name_port2] = device1

            elif device1_Type == 2 and device2_Type == 2:
                self.connections[name_port1] = device2
                self.connections[name_port2] = device1
    
        return error_type_name_port1, error_type_name_port2

    #def __connect_pc_pc(self, pc_1 : Objs.Computer, pc_2 : Objs.Computer):
    #   if pc_1.connections[0] != None or pc_2.connections[0] != None:
    #        return False
    #
    #    pc_1.connections.append(pc_2)
    #    pc_2.connections.append(pc_1)
    #    return True
    
    #def connect(por1:str,port2:str):
    #    if port1 not in Objs.ports.keys():
    #        print(f"Error the port {port1} not exist")
    #    elif port2 not in Objs.ports.keys():
    #        print(f"Error the port {port2} not exist")
    #    else:
    #        Objs.ports[port1].connect(por2)

    #def __connect_hub_hub(self, hub_1 : Objs.Hub, hub_2 : Objs.Hub,port_hub_1 : int, port_hub_2 : int):
    #    if hub_1[port_hub_1] != None or hub_2[port_hub_2] != None:
    #        return False

    #    hub_2.connections[port_hub_2] = hub_1  
    #    hub_1.connections[port_hub_1] = hub_2
    #    return True

    #def __connect_hub_pc(self, hub : Objs.Hub, pc : Objs.Computer, hub_port : int):
    #    if hub.connections[hub_port] != None or pc.connections[0] != None:
    #        return False
    #    hub.connections[hub_port] = pc
    #    pc.connections[0] = hub
    #    return True

    def shutdown_connection(self, name_port):
        #error_type 3 => the port is not connected
        error_type = False
        error_type, device = self.__validate_disconnection(name_port)

        if(error_type):
            self.connections[name_port] = None

        return error_type

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
            

      