import sys, argparse
import device_handler as dh
import myParser

def main():
    
    handler = dh.Device_handler()
    parser = argparse.ArgumentParser(description="Instrucciones del script")
    errors = {1 : "port is busy",
              2 : "port does not exist",
              3 : "port is free"
    }
    caller ={
        "create hub" : lambda name, ports_amount :  handler.create_hub(name, ports_amount),
        "create host" : lambda name : handler.create_pc(name),
        "connect" : lambda args : handler.setup_connection(args[0],args[1]),
        #"send" : lambda args : send_connect(args),
        "disconnect" : lambda args :  handler.shutdown_connection(args[0])
        }
    parser.add_argument('-f', dest='textfile', default=True)
    args = parser.parse_args()
    filename = args.textfile
    f = open(filename, 'r')
    for line in f.readlines():
        instruction, args2 = myParser.parse(line)
        if(instruction == "create hub" or instruction == "create host"):
            caller[instruction](args2)

        if(instruction == "connect"):
            error_type_port1, error_type_port2 = caller[instruction](args2)
            if(error_type_port1 and error_type_port2):
                print(f"{args2[0]} {errors[error_type_port1]}")
                print(f"{args2[1]} {errors[error_type_port2]}")

        if(instruction == "disconnect"):
            error_type = caller[instruction](args2)
            if(error_type):
                print(f"{args2[0]} {errors[error_type]}")

        if(instruction == "send"):
            pass
            
        

if __name__== "__main__":
    main()
