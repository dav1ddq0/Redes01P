from enum import Enum

ports = {}

class Status(Enum):
    Null = 2
    One = 1
    Zero = 0

class Port:
    def __init__(self, name:str, parent):
        self.name = name
        self.cable_data = None
        self.cable_connected = False
        self.parent = parent
        self.time = 0

    #def Stopwatcher(self):
    #    if time !=0:
    #        self.time -=1
    #        if time ==0:
    #            self.data=None
               

class Computer:
    def __init__(self, name:str) -> None:
        self.name = name
        self.connections = [None]*1
        portname = f"{name}_1"
        port = Port(portname, self)
        ports["portname"]= port
        self.port = port
        self.file = f"{name}.txt"
        f = open(self.file, 'w')
        f.close()
    
    def UpdateFile(self, message):
        f = open(self.file, 'w')
        f.write(message)
        f.close()
    
    def Log(self, data, action, time=0):
        message = f"{time} {self.port} {action} {data}"
        self.UpdateFile(message)

class Hub:
    def __init__(self, name:str, ports_amount : int) -> None:
        self.name = name
        self.connections = [None]*ports_amount
        self.file = f"{name}.txt"
        self.ports=[] # instance a list of ports
        for i in range(ports_amount):
            portname = f"name_{i+1}"
            port = Port(portname, self)
            self.ports.append(port)
            ports[portname] = port
        #make the hub file
        f = open(self.file, 'w')
        f.close()

    def UpdateFile(self, name, message):
        f=open(self.file,'w')
        f.write(message)
        f.close()    

    def Log(self, data, action, port, time=0):
        message = f"{time} {port} {action} {data}"
        self.UpdateFile(message)

