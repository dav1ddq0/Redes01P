from enum import Enum

ports = {}
transmition_time = 3
class Status(Enum):
    Null = 2
    One = 1
    Zero = 0


class Cable:
    def __init__(self):
        self.data = None # 0 1 None son los tres estados en los que puede estar el cable
        # puerto de donde se esta enviando la informacion
        # es muy util para cuando haya que desconectar
        self.port = None

class Port:
    def __init__(self, name:str, parent):
        self.name = name
        self.cable = None
        self.parent = parent
        self.time = 0

class Computer:
    def __init__(self, name:str) -> None:
        self.name = name
        portname = f"{name}_1"
        port = Port(portname, self)
        ports[portname] = port
        self.port = port
        self.file = f"{name}.txt"
        self.data = None
        self.time_remaining = 0
        self.sending=False
        f = open(self.file, 'w')
        f.close()
    
    def UpdateFile(self, message):
        f = open(self.file, 'a')
        f.write(message)
        f.close()
    
    def Log(self, data, action, time=0):
        message = f"{time} {self.port.name} {action} {data}\n"
        self.UpdateFile(message)

    def Stopwatcher(self):
        if self.time_remaining != 0:
            self.time_remaining -= 1    


    def Next_Bit(self):
        n=len(self.data)
        if n > 0:
            next = self.data[n-1]
            self.data = self.data[0:n-1]
            self.time_remaining=transmition_time
            return next
        return None    
        
class Hub:
    def __init__(self, name: str, ports_amount: int) -> None:
        self.name = name
        self.connections = [None]*ports_amount
        self.file = f"{name}.txt"
        self.ports = []  # instance a list of ports
        self.time_remaining = 0 
        for i in range(ports_amount):
            portname = f"{name}_{i+1}"
            port = Port(portname, self)
            self.ports.append(port)
            ports[portname] = port
        #make the hub file
        f = open(self.file, 'w')
        f.close()


    def Stopwatcher(self):
        if self.time_remaining != 0:
            self.time_remaining -= 1  

    def UpdateFile(self,  message):
        f=open(self.file,'a')
        f.write(message)
        f.close()    

    def Log(self, data, action, port, time=0):
        message = f"{time} {port} {action} {data}\n"
        self.UpdateFile(message)

