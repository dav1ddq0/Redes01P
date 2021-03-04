handler = None

caller ={
        "create":lambda args:create_call(args),
        "hub": lambda name, ports_amount :  handler.create_hub(name,ports_amount),
        "host" : lambda name : handler.create_pc(name),
        "connect" : lambda args:connect_call(args),
        "send" :lambda args : send_connect(args),
        "disconnect":lambda args :  disconnect_call(args)
        }


# the possible instructions to execute are create,connect,send,disconnect
def validInst(inst:str):
    return inst != "create" and inst != "connect" and inst != "send" and inst != "disconnect"

def create_call(args:list):
    if args[0] == "hub":
        ports_amount = 0
        try :
            ports_amount = int(args[2])
            name =args[1]
            if len(args) == 3:
                caller["hub"](name,ports_amount)    
        except ValueError:
            print("Invalid parameter")
    if args[0] == "host":
        if len(args) == 2:
            name=args[1]
            caller["host"](name)
        else:
            print("Invalid number of args ")

def connect_call(args:list):
    if len(args) != 2 :
        print("Invalid args count ")
        
    else:
        port1=args[0]
        port2=args[2]
        handler.connect(por1,port2)
        

def disconnect_call(args:list):
    if len(args) != 1:
        print("Invalida count of args ")
    else:
        port=args[0]
        handler.disconnect(port)