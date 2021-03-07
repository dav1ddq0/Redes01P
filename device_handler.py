from os import name, stat
import Objs


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

    def __validate_send(self, name_port):
        port = Objs.ports[name_port]
        if not isinstance(port.parent, Objs.Computer):
            print(f"port {name_port} {errors[4]}")
            return False

        elif name_port not in Objs.ports.keys():
            print(f"port {name_port} {errors[2]}")
            return False

        elif not port.cable_connected:
            print(f"port {name_port} {errors[1]}")
            return False

        elif name_port not in self.connections.keys():
            print(f"port {name_port} {errors[6]}")
            return False

        return True

    def __validate_disconnection(self, name_port):
        port = Objs.ports[name_port]

        if name_port not in Objs.ports.keys():
             print(f"port {name_port} {errors[2]}")
             return False

        elif not port.cable_connected:
                print(f"port {name_port} {errors[1]}")
                return False

        return True

    def __validate_connection(self, name_port): #Private method to identify wether a device is a hub or a host
        port = Objs.ports[name_port]

        if name_port not in Objs.ports.keys():
            print(f"port {name_port} {errors[2]}")
            return False

        elif  port.cable_connected:
                print(f"Port{name_port} {errors[3]}")
                return False

        return True

    def upgrade_network_state(time: int):
        while self.time < time and len(self.host_sending) > 0:
            self.time += 1
            self.update_host_sending()
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
            self.connections[name_port1] = name_port2
            self.connections[name_port2] = name_port1
            port1.cable_connected = True
            port2.cable_connected = True

    def shutdown_connection(self, name_port: str, time: int):
        self.upgrade_network_state(time)

        if self.__validate_disconnection(name_port):
            port1 = Objs.ports[name_port]
            port1.cable_connected = False
            name2, port2 = self.connections[name_port]
            del self.connections[name_port]
            del self.connections[f"{name2}_{port2}"]

    def update_host_sending(self):
        for host in self.host_sending:
            host.Stopwatcher()
            if host.time_remaining == 0:
                nex_bit = host.send()
                if nex_bit == None:
                    self.host_sending.remove(host)
                else:
                    self.send_bit(self, host.port, nex_bit)



    def send(self, origin_pc, data):
        self.upgrade_network_state(time)

        if self.__validate_send_bit(origin_pc):  # El send es valido
            host = Objs.ports[origin_pc].parent
            host.time_remaining = Objs.transmition_time
            self.host_sending.append(host)
            nex_bit = host.send()
            self.send_bit(self, origin_pc, nex_bit)

            

    def send_bit(self, origin_pc, data):
        device = Objs.ports[origin_pc].parent
        device.Log(data, "send",self.time)
        device.port.cable_data = data
        destination_device, destination_port = Objs.ports[self.connections[origin_pc]].parent, Objs.ports[self.connections[origin_pc]]
        self.__spread_data(destination_device, data, Objs.ports[destination_port])



    def __spread_data(self, device, data, data_incoming_port):

        if isinstance(device, Objs.Computer):
            device.port.cable_data = data
            device.Log(data, "send",self.time)

        elif isinstance(device, Objs.Hub):
            device.Log(data, "receive", data_incoming_port.name, self.time)
            for port in device.ports:
                device.Log(data, "send", port.name, self.time)
                port.cable_data = data
                if port != data_incoming_port:
                    next_device, next_port = Objs.ports[self.connections[port.name]].parent, Objs.ports[self.connections[port.name]]
                    self.__spread_data(next_device, data, next_port)
                    




            

      
