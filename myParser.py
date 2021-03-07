caller ={
        "create" : lambda args : create_parse(args) ,
        "connect" : lambda args : connect_parse(args),
        "send" : lambda args : send_parse(args),
        "disconnect" : lambda args :  disconnect_parse(args)
        }

# parse de linne of the file
def parse(line : str):
    #remove the line jump
    line = line.replace('\n','')
    #divide the line in tokens
    codes = line.split(' ')
    instruction_time = 0
    try :
        instruction_time = int(codes[0])
    except ValueError:
        print("Invalid parameter")

    codes = codes[1:]

    if codes[0] not in caller.keys():
        print(f"{codes[0]} is invalid command")
        return
    else:
        return caller[codes[0]]

def __check_binary(string):
    s = set(string)
    p = {0 , 1}

    if s == p or p == {'0'} or p == {'1'}:
        return True

    return False

def create_parse(args : list):
    if args[1] == "hub":
        ports_amount = 0
        try :
            ports_amount = int(args[3])
        except ValueError:
            print("Invalid parameter")
        if len(args) == 4:
                # hub,name,ports_amount
                return args[1], args[2], ports_amount
        else : print("Invalid amount of arguments")
        
    elif args[1] == "host":
        if len(args) == 3:
            return args[1], args[2]
            
        else : print("Invalid amount of arguments")


def connect_parse(args : list):

    if args[1].find('_') != -1 and args[2].find('_') != -1:
            _, device1_port = args[1].split('_')
            _, device2_port = args[2].split('_')

            try:
                device1_port = int(device1_port)
                device2_port = int(device2_port)
            except ValueError:
                print("Invalid parameters")
            
            if len(args) == 3:
                # connect,port1,port2
                return args[0], args[1], args[2]
            else : print("Invalid amount of arguments")

def send_parse(args:list):
    if args[1].find('_'):
        _, device1_port = args[1].split('_')
        try:
            device1_port = int(device1_port)
        except ValueError:
            print("Invalid parameters")
        if len(args) == 3:
            if __check_binary(args[2]):
                return args[0], args[1], args[2]
            else : print("The data to send must be a binary code")

# sintax error of insr time disconnect
def disconnect_parse(args:list):
    if args[1].find('_'):
        _, device_port = args[1].split('_')
            
        try:
            device_port = int(device_port)
        except ValueError:
            print("Invalid parameters")
        if len(args) == 2: 
            # disconnect,port
            return args[0], args[1]
        else : print("Invalid amount of arguments")
    else:
        print("Invalid format")    