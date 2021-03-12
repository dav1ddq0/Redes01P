from os import name, stat
import objs
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
        self.hosts = []
        self.connections = {}
        self.time = 0
        self.transmition_time = 3
        # diccionario que va a guardar todos los puertos de todos los devices para poder acceder de manera rapida a los mismo en 
        # las operaciones necesarias
        self.ports = {}

    def __validate_send(self, host):

        port_name = host+"_1"
        if port_name not in self.ports.keys():
            print(f"port {port_name} {errors[2]}")
            return False

        port = self.ports[port_name]
        if not isinstance(port.device, objs.Host):
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
        port = self.ports[name_port]

        if name_port not in self.ports.keys():
             print(f"port {name_port} {errors[2]}")
             return False

        elif port.cable == None:
                print(f"port {name_port} {errors[1]}")
                return False

        return True

    def __validate_connection(self, name_port): #Private method to identify wether a device is a hub or a host
        

        if name_port not in self.ports.keys():
            print(f"port {name_port} {errors[2]}")
            return False
        port = self.ports[name_port]
        if  port.cable != None:
                print(f"Port{name_port} {errors[3]}")
                return False

        return True

    def finished_network_transmission(self):    
        while True:
            self.time += 1
            if not self.update_devices():
                break

    def upgrade_network_state(self, time: int):
        while self.time <= time:
            self.time += 1
            self.update_devices()
        self.time = time

    def create_pc(self, name: str, time: int):
        self.upgrade_network_state(time)
        newpc = objs.Host(name)
        self.hosts.append(newpc)
        self.ports[newpc.port.name] = newpc.port

    def create_hub(self, name: str, ports, time: int):
        self.upgrade_network_state(time)
        self.time = time    
        newhub = objs.Hub(name, ports)
        for port in newhub.ports:
            self.ports[port.name] = port

    def setup_connection(self, name_port1: str, name_port2: str, time: int):
        self.upgrade_network_state(time)

        if self.__validate_connection(name_port1) and self.__validate_connection(name_port2):
            port1 = self.ports[name_port1]
            port2 = self.ports[name_port2]
            device1 = port1.device
            device2 = port2.device
            if device1 == device2:
                print("Ports of the same device is not possible connected")
                
            else:
                self.connections[name_port1] = name_port2
                self.connections[name_port2] = name_port1
                newcable = objs.Cable()
                port1.cable = newcable
                port2.cable = newcable
                # si los dispositvos pertencientes a los puertos estan transmitiendo informacion a la vez
                #
                # en caso que conecte un hub a otro hub que estan retransmitiendo la informacion desde distintos host
                if device1.bit_sending != None and device2.bit_sending != None:
                    self.walk_clean_data_cable(device1)
                    self.walk_clean_data_cable(device2)
                elif device1.bit_sending != None:
                    port1.cable.data = device1.bit_sending
                    self.__spread_data(device2, device1.bit_sending, port2)
                elif device2.bit_sending != None:
                    port2.cable.data = device1.bit_sending
                    self.__spread_data(device1, device2.bit_sending, port1)
                

       



    # hay que remover los datos de los cables que se quedaron desconectados del host que estaba enviando informacion
    def walk_clean_data_cable(self, device, incoming_port:objs.Port):
        # en caso que llegue a una PC es porque no tengo
        # que seguir verificando conexiones muertas pues la pc solo puede enviar o recibir 
        if isinstance(device, objs.Host):
            if device.transmitting:
                device.stopped = True
                device.transmitting = False
                # notifica que hubo una colision y la informacion no pudo enviarse
                device.Log(device.bit_sending, "send", self.time, True)
                # el rango se duplica en cada intento fallido
                if device.failed_attempts < 16:
                    nrand =  random.randint(1, 2*device.failed_attempts*10)
                    # dada una colision espero un tiempo cada vez mayor para poder volverla a enviar
                    device.time_stopped = nrand * self.transmition_time
                else:
                    # se cumplio el maximo de intentos fallidos permitidos por lo que se decide perder esa info
                    device.bit_sending = None
                    device.stopped = False
                    device.failed_attempts = 0
            return
    
        elif isinstance(device, objs.Hub):
            device.bit_sending = None
            for port in device.ports:
                if port.cable != None and port != incoming_port:
                    port.cable.data = objs.Data.Null
                    if port.name in self.connections.keys():
                        portname2 = self.connections[port.name]
                        port2 = self.ports[portname2]
                        self.walk_clean_data_cable(port2.device,port2)

    def shutdown_connection(self, name_port: str, time: int):
        self.upgrade_network_state(time)

        if self.__validate_disconnection(name_port):
            port1 = self.ports[name_port]
            name_port2 = self.connections[name_port]
            port2 = self.ports[name_port2]
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
        for host in self.hosts:
            # en caso que el host no haya podido enviar una informacion previamente producto de una colision
            # por la forma del carrier senses el va a esperar un tiempo aleatorio entre 4 y 10ms para volver
            # a intentar enviar esa informacion
            if host.stopped:
                host.time_stopped -=1
                if host.time_stopped == 0:
                    host.stopped = False
                    # vuelve a intentar enviar el bit que habia fallado previamente
                    self.send_bit(host,host.bit_sending)
                return True

            if host.transmitting:
                host.transmitting_time +=1
                if host.transmitting_time % self.transmition_time == 0:
                    nex_bit = host.Next_Bit()
                    if nex_bit != None:
                        host.bit_sending = nex_bit
                    else:
                        host.bit_sending = -1

                    if host.port.name in self.connections.keys():
                        portname2 = self.connections[host.port.name]
                        port2 = self.ports[portname2]
                        # limpia el camino para enviar el proximo bit
                        self.walk_clean_data_cable(port2.device,port2)

                    if nex_bit == None and host.data_pending.qsize() > 0:
                        # obtengo la proxima cadena de bits a transmitir sacando el proximo elemento de la cola
                        host.data = host.data_pending.get()          
                        nex_bit = host.Next_Bit()
                                                
                    if nex_bit != None:
                        if host.port.cable != None:
                            host.port.cable.data = objs.Data.Null
                        self.send_bit(host,nex_bit)
                    else:
                        host.bit_sending = None
                        host.transmitting = False    
                
                return True    

        return False                



    def send(self, origin_pc, data, time):
        # actualiza primero la red por si todavia no ha llegado a time 
        self.upgrade_network_state(time)

        if self.__validate_send(origin_pc):  # El send es valido
            host = self.ports[origin_pc+'_1'].device
            # en caso que la pc este transmitiendo otra informacion
            if host.data != None:
                # agrego esa nueva informacion a una cola de datos sin enviar
                host.data_pending.put(data)
            else:
                host.data = data
                nex_bit = host.Next_Bit()
                self.send_bit(host, nex_bit)

            

    # Metodo que se encarga de intentar enviar un bit desde una PC
    def send_bit(self, origin_pc, data):
        
        device = origin_pc
        device.bit_sending = data
        
        if not device.Put_Data(data):
                # el host no puede enviar en este momento la sennal pues se esta transmitiendo informacion por el canal o no tiene canal para transmitir la informacion
                device.stopped = True
                # aumenta la cantidad de intentos fallidos
                device.failed_attempts += 1 
                # notifica que hubo una colision y la informacion no pudo enviarse
                device.Log(data, "send", self.time, True)
                # el rango se duplica en cada intento fallido
                if device.failed_attempts < 16:
                    nrand =  random.randint(1, 2*device.failed_attempts*10)
                    # dada una colision espero un tiempo cada vez mayor para poder volverla a enviar
                    device.time_stopped = nrand * self.transmition_time
                else:
                    # se cumplio el maximo de intentos fallidos permitidos por lo que se decide perder esa info
                    device.bit_sending = None    
        else:
            device.transmitting = True
            device.transmitting_time = 0
            device.Log(data, "send",self.time)
            # revise el object del puerto 
            destination_port = self.ports[self.connections[origin_pc.port.name]]
            destination_device =destination_port.device
            self.spread_data(destination_device, data, destination_port)



    def spread_data(self, device, data, data_incoming_port):

        if isinstance(device, objs.Host):
            # en caso que la informacion llegue a una pc que deberia de estar transmitiendo
            # if device.bit_sending != None and not device.stopped:
            #     device.Log(data, "receive", self.time, True)
            #     device.bit_sending = None
            # else:
            device.Log(data, "receive", self.time)
            
        elif isinstance(device, objs.Hub):
            device.bit_sending = data
            device.Log(data, "receive", data_incoming_port.name, self.time)
            for port in device.ports:
                if port != data_incoming_port and port.cable != None:
                    port.cable.data = data
                    port.cable.port = port
                    # para seguir de forma recursiva por ese puerto es necesario primero verificar que este  este conectado con otro puerto a traves de un cable
                    # para eso verifico que este en dicc connections pues este guarda todas las conexiones entre puertos a traves de un cable
                    if port.name in self.connections.keys(): # en caso que este puerto conecte con otro de otro device
                        device.Log(data, "send", port.name, self.time)
                        next_port  = self.ports[self.connections[port.name]]
                        next_device = self.ports[self.connections[port.name]].device
                        # sigue regando la informacion a otros devices
                        self.spread_data(next_device, data, next_port)
                    




            

      
