from os import name, stat
import Objs
import random

errors = {  1 : "is free",
            2 : "does not exist",
            3 : "is not free",
            4 : "the device must be a host",
            5 : "host busy (collision)",
            6 : "has a cable connected, but its other endpoint is not connected to another device"
        }
class Device_handler:
    # @property
    # def hosts(self):
    #     return self.hosts

    def __init__(self) -> None:
        self.hubs = []
        self.hosts = []
        self.connections = {}
        self.host_sending = []
        self.time = 0

    def __validate_send(self, host):

        port_name = host+"_1"
        if port_name not in Objs.ports.keys():
            print(f"port {port_name} {errors[2]}")
            return False

        port = Objs.ports[port_name]
        if not isinstance(port.parent, Objs.Computer):
            print(f"port {port_name} {errors[4]}")
            return False

        elif port.cable == None:
            print(f"port {port_name} {errors[1]}")
            return False

        elif port.name not in self.connections.keys():
            print(f"port {name_port} {errors[6]}")
            return False

        return True

    def __validate_disconnection(self, name_port):
        port = Objs.ports[name_port]

        if name_port not in Objs.ports.keys():
             print(f"port {name_port} {errors[2]}")
             return False

        elif port.cable == None:
                print(f"port {name_port} {errors[1]}")
                return False

        return True

    def __validate_connection(self, name_port): #Private method to identify wether a device is a hub or a host
        

        if name_port not in Objs.ports.keys():
            print(f"port {name_port} {errors[2]}")
            return False
        port = Objs.ports[name_port]
        if  port.cable != None:
                print(f"Port{name_port} {errors[3]}")
                return False

        return True

    def finished_network_transmission(self):
        while len(self.host_sending) > 0:
            self.time += 1
            self.update_devices()

    def upgrade_network_state(self, time: int):
        while self.time < time:
            self.time += 1
            self.update_devices()
        self.time = time

    def create_pc(self, name: str, time: int):
        self.upgrade_network_state(time)
        newpc = Objs.Computer(name)
        self.hosts.append(newpc)

    def create_hub(self, name: str, ports, time: int):
        self.upgrade_network_state(time)
        self.time = time    
        newhub = Objs.Hub(name, ports)
        self.hubs.append(newhub)

    def setup_connection(self, name_port1: str, name_port2: str, time: int):
        self.upgrade_network_state(time)

        if self.__validate_connection(name_port1) and self.__validate_connection(name_port2):
            port1 = Objs.ports[name_port1]
            port2 = Objs.ports[name_port2]
            device1 = port1.parent
            device2 = port2.parent
            if device1 == device2 or port1 == port2:
                print("Ports of the same device is not possible connected")
                
            else:
                self.connections[name_port1] = name_port2
                self.connections[name_port2] = name_port1
                newcable = Objs.Cable()
                port1.cable = newcable
                port2.cable = newcable
                # si los dispositvos pertencientes a los puertos estan transmitiendo informacion a la vez
                #
                if device1.bit_sending != None and device2.bit_sending != None:
                    # en este caso de forma aleatoria se decide que informacion se mantendra en transmision
                    # y cual se pierde
                    rnumb = random.randint(0,100)
                    if rnumb % 2 == 0:
                        port1.cable.data = device1.bit_sending
                        self.__spread_data(device2, device1.bit_sending, port2)
                    else:
                        port2.cable.data = device1.bit_sending
                        self.__spread_data(device1, device2.bit_sending, port1)

                elif device1.bit_sending != None:
                        port1.cable.data = device1.bit_sending
                        self.__spread_data(device2, device1.bit_sending, port2)
                elif device2.bit_sending != None:
                        port2.cable.data = device1.bit_sending
                        self.__spread_data(device1, device2.bit_sending, port1)
                



            



    # hay que remover los datos de los cables que se quedaron desconectados del host que estaba enviando informacion
    def walk_clean_data_cable(self, device):
        # en caso que llegue a una PC es porque no tengo
        # que seguir verificando conexiones muertas pues la pc solo puede enviar o recibir 
        if isinstance(device, Objs.Computer):
            device.port.data = None
            return
    
        elif isinstance(device, Objs.Hub):
            for port in device.ports:
                if port.cable != None and port.cable.data != None:
                    port.cable.data = None
                    if port.name in self.connections.keys():
                        portname2 = self.connections[port.name]
                        port2 = Objs.ports[portname2]
                        self.walk_clean_data_cable(port2.parent)

    def shutdown_connection(self, name_port: str, time: int):
        self.upgrade_network_state(time)

        if self.__validate_disconnection(name_port):
            port1 = Objs.ports[name_port]
            name_port2 = self.connections[name_port]
            port2 = Objs.ports[name_port2]
            # si por este cable no esta pasando informacion actualmente
            if port1.cable.data != None:
                if port1.cable.port != port1:
                    self.walk_clean_data_cable(port2.parent)
                else:
                    self.walk_clean_data_cable(port1.parent)
            # tengo que remover el cable del puerto port1 
            port1.cable = None        
            del self.connections[name_port]
            del self.connections[name_port2]

    # de esta forma se revisa si host que esta transmitiendo dejo de hacerlo y por ende toda la informacion desaparece de los cables
    # a los que pueda llegar desde el otra
 
    def update_devices(self):    
        for host in self.host_sending:
            host.Stopwatcher()
            if host.time_remaining == 0:
                host.bit_sending = None
                
                if host.port.cable != None:
                    host.port.cable.data = None
                
                if host.port.name in self.connections.keys():
                    portname2 = self.connections[host.port.name]
                    port2 = Objs.ports[portname2]
                    self.walk_clean_data_cable(port2.parent)
                    
                nex_bit = host.Next_Bit()
                if nex_bit == None:
                    if host.data_pending.qsize() > 0:
                        # obtengo la proxima cadena de bits a transmitir sacando el proximo elemento de la cola
                        host.data = host.data_pending.get()
                        nex_bit = host.Next_Bit()
                        self.send_bit(host,nex_bit)

                    else:
                        self.host_sending.remove(host)
                        
                        
                else:
                    if host.port.cable != None:          
                        self.send_bit(host,nex_bit)


    def send(self, origin_pc, data, time):
        self.upgrade_network_state(time)

        if self.__validate_send(origin_pc):  # El send es valido
            host = Objs.ports[origin_pc+'_1'].parent
            # en caso que la pc este transmitiendo otra informacion
            if host.data != None:
                # agrego esa nueva informacion a una cola de datos sin enviar
                host.data_pending.put(data)
            else:
                host.time_remaining = Objs.transmition_time
                self.host_sending.append(host)
                host.data = data
                nex_bit = host.Next_Bit()
                self.send_bit(host, nex_bit)

            


    def send_bit(self, origin_pc, data):
        device = origin_pc
        if device.bit_sending != None:
                device.Log(data, "send", self.time, True)
        else:
            device.bit_sending = data
            device.port.cable.data = data
            device.Log(data, "send",self.time)
            destination_device = Objs.ports[self.connections[origin_pc.port.name]].parent
            destination_port = Objs.ports[self.connections[origin_pc.port.name]]
            self.__spread_data(destination_device, data, destination_port)



    def __spread_data(self, device, data, data_incoming_port):

        if isinstance(device, Objs.Computer):
            if device.bit_sending != None:
                device.Log(data, "receive", self.time, True)
                device.bit_sending = None
            else:
                device.Log(data, "receive", self.time)
            
        elif isinstance(device, Objs.Hub):
            device.bit_sending = data
            device.Log(data, "receive", data_incoming_port.name, self.time)
            for port in device.ports:
                if port != data_incoming_port and port.cable != None:
                    port.cable.data = data
                    port.cable.port = port
                    # para seguir de forma recursiva por ese puerto es necesario primero verificar que este  este conectado con otro puerto a traves de un cable
                    # para eso verifico que este en dicc connections pues este guarda todas las conexiones entre puertos a traves de un cable
                    if port.name in self.connections.keys():
                        device.Log(data, "send", port.name, self.time)
                        next_device = Objs.ports[self.connections[port.name]].parent
                        next_port  = Objs.ports[self.connections[port.name]]
                        self.__spread_data(next_device, data, next_port)
                    




            

      
