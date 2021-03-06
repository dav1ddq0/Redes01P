from enum import Enum

ports_d={}

class Status(Enum):
    Host = 1
    Hub  = 2
class Port:
    def __init__(self, name:str,parent,type:Status):
        self.name = name
        self.cable = None
        self.cable_connected=False
        self.next = None
        self.parent=parent
        self.type=Status
        self.time=0

    def Stopwatcher(self):
        if time !=0:
            self.time -=1
            if time ==0:
                self.data=None
               

class Computer:
    def __init__(self, name:str) -> None:
        self.name = name
        self.connections = [None]*1
        portname=f"{name}_1"
        port = Port(portname,self,Status.Host)
        ports_d["portname"]=port
        self.port = port
        self.file=f"{name}.txt"
        f=open(self.file,'w')
        f.close()
        self.data=None
    
    def UpdateFile(self,message):
        f=open(self.file,'w')
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
            port = Port(portname,self,Status.Hub)
            self.ports.append(port)
            ports_d[portname]=port
        #make the hub file
        f=open(self.file,'w')
        f.close()

    def UpdateFile(self,name,message):
        f=open(self.file,'w')
        f.write(message)
        f.close()    
    
