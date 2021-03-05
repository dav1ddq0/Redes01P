def parse(line):
    line = line.replace('\n','')
    codes = line.split(' ')
    instruction_time = 0

    try :
        instruction_time = int(codes[0])
    except ValueError:
        print("Invalid parameter")

    codes = codes[1:]
    if codes[0] == "create":
        if codes[1] == "hub":
            ports_amount = 0
            try :
                ports_amount = int(codes[3])
            except ValueError:
                 print("Invalid parameter")

            if len(codes) == 4:
                    return "create hub", codes[2], ports_amount
            else : print("Invalid amount of arguments")
            
        if codes[1] == "host":
            if len(codes) == 3:
                return "create host", codes[2]
            else : print("Invalid amount of arguments")

    elif codes[0] == "connect":
        if codes[1].find('_') != -1 and codes[2].find('_') != -1:
            device1_name, device1_port = codes[1].split('_')
            device2_name, device2_port = codes[2].split('_')

            try:
                device1_port = int(device1_port)
                device2_port = int(device2_port)
            except ValueError:
                print("Invalid parameters")
            
            if len(codes) == 3:
                return codes[0], codes[1], codes[2]
            else : print("Invalid amount of arguments")
            

    elif codes[0] == "disconnect":
        if codes[1].find('_'):
            device_name, device_port = codes[1].split('_')
                
            try:
                device_port = int(device_port)
            except ValueError:
                print("Invalid parameters")

            if len(codes) == 2: 
                return codes[0], codes[1]
            else : print("Invalid amount of arguments")
    
    elif codes[0] == "send":
        if codes[1].find('_'):
            device_name, device_port = codes[1].split('_')

            try:
                device_port = int(device_port)
            except ValueError:
                print("Invalid parameters")

            if len(codes) == 3:
                if __check_binary(codes[2]):
                    return codes[0], codes[1], codes[2]
                else : print("The data to send must be a binary code")
                      
def __check_binary(string):
    p = set(string)
    s = {0 , 1}

    if s == p or p == {'0'} or p == {'1'}:
        return True

    return False

#
#
## the possible instructions to execute are create,connect,send,disconnect
#def validInst(inst:str):
#    return inst != "create" and inst != "connect" and inst != "send" and inst != "disconnect"
#
#def create_call(args:list):
#    if args[0] == "hub":
#        ports_amount = 0
#        try :
#            ports_amount = int(args[2])
#            name =args[1]
#            if len(args) == 3:
#                caller["hub"](name,ports_amount)    
#        except ValueError:
#            print("Invalid parameter")
#    if args[0] == "host":
#        if len(args) == 2:
#            name=args[1]
#            caller["host"](name)
#        else:
#            print("Invalid number of args")
#
#def connect_call(args):
#    if len(args) == 2 and args[1].find('_') != -1 and args[2].find('_') != -1:
#        device1_name, device1_port = args[1].split('_')
#        device2_name, device2_port = args[2].split('_')
#        try:
#            device1_port = int(device1_port)
#            device2_port = int(device2_port)
#            handler.connect(device1_port,device2_port)
#        except ValueError:
#            print("Invalid parameters")
#    else :
#        print("Invalid amount of arguments")
#
#def connect_call(args:list):
#    if len(args) != 2 :
#        print("Invalid args count ")
#        
#    else:
#        port1=args[0]
#        port2=args[2]
#        
#        
#
#def disconnect_call(args:list):
#    if len(args) != 1:
#        print("Invalida count of args ")
#    else:
#        port=args[0]
#        handler.disconnect(port)