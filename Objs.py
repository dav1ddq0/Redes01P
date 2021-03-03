import os
class Computer:
    def __init__(self, name) -> None:
        self.name = name
        self.connections = [None]*1
        self.file=f"{name}.txt"
        f=open(self.file,'w')
        f.close()
    
    def UpdateFile(self,name,message):
        f=open(self.file,'w')
        f.write(message)
        f.close()
class Hub:
    def __init__(self, name, ports_amount : int) -> None:
        self.name = name
        self.connections = [None]*ports_amount
        self.file=f"{name}.txt"
        f=open(self.file,'w')
        f.close()

    def UpdateFile(self,name,message):
        f=open(self.file,'w')
        f.write(message)
        f.close()    