from enum import Enum
class Status(Enum):
    Host = 1
    Hub  = 2
class Port:
    def __init__(self, name:str,type:Status):
        self.name = name
        self.cable = False
        self.next = None
        self.type=Status
        self.time=0

    def Stopwatcher(self):
        if time !=0:
            self.time -=1
            if time ==0:
                self.data=None
            
    #def connect(self,other_port):
    #    if self.next != None:
    #        print(f"Sorry the port {self.name} is already connected with {self.next}")
    #    elif self.cable == True:
    #        print("Sorry this port have a trash cable connected")
    #    elif other_port.cable==True:
    #        print("Sorry the port {other_port}  port have a trash cable connected")
    #    elif  other_port.next!=None:
    #        print("Sorry the port  {other_port} is already connected with {other_port.next}")
    #    else:
    #        self.cable=True
    #        self.next=other_port
    #        other_port.next=self.name
    #        other_port.cable=True
    #
    #def disconnect(self):
    #    self.cable=False
    #    self.next.next=None
    #    self.next=None        

class Computer:
    def __init__(self, name:str) -> None:
        self.name = name
        self.connections = [None]*1
        portname=f"{name}_1"
        port = Port(portname,Status.Host)
        self.port = port
        self.file=f"{name}.txt"
        f=open(self.file,'w')
        f.close()
        self.data=None
    
    def UpdateFile(self,message):
        f = open(self.file,'w')
        f.write(message)
        f.close()
    
    def Log(self,time,data,action):
        message=f"{time} {self.port} {action} {data}"
        UpdateFile(message)

class Hub:
    def __init__(self, name:str, ports_amount : int) -> None:
        self.name = name
        self.connections = [None]*ports_amount
        self.file=f"{name}.txt"
        self.ports=[] # instance a list of ports
        for i in range(ports_amount):
            portname = f"name_{i+1}"
            port = Port(portname,Status.Hub)
            self.ports.append(port)
        #make the hub file
        f=open(self.file,'w')
        f.close()

    def UpdateFile(self,name,message):
        f=open(self.file,'w')
        f.write(message)
        f.close()    
    
