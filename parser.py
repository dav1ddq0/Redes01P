handler = None

caller ={
        "create":lambda args:create_call(args),
        "hub": lambda name, ports_amount :  handler.create_hub(name,ports_amount),
        "host" : lambda name : handler.create_pc(name),
        "connect" : lambda args:connect_call(args),
        #"send" :lambda args : send_connect(args),
        "disconnect":lambda args :  disconnect_call(args)
        }


# the possible instructions to execute are create,connect,send,disconnect
def validInst(inst:str):
    return inst != "create" and inst != "connect" and inst != "send" and inst != "disconnect"

def create_call(args:list):
    print(args)
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
            print("Invalid number of args")

def connect_call(args):
    if len(args) == 3 and args[1].find('_') != -1 and args[2].find('_') != -1:
        device1_name, device1_port = args[1].split('_')
        device2_name, device2_port = args[2].split('_')
        try:
            device1_port = int(device1_port)
            device2_port = int(device2_port)
            handler.setup_device_connection(device1_name, device2_name, device1_port, device2_port)
        except ValueError:
            print("Invalid parameters")
        

def disconnect_call(args):
    if len(args) == 2 and args[1].find('_'):
        device_name, device_port = args[1].split('_')
        
        try:
            device_port = int(device_port)
        except ValueError:
            print("Invalidad parameters")
        handler.shutdown_device_connection(device_name, device_port)