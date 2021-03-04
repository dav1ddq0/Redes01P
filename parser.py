import sys,argparse
import os
import device_handler as dh

# <time> create hub <name> <cantidad de puertos>
# <time> create host <name>
# <time> connect <port1> <port2>
# <time> send <host> <data>
# <time> disconnect <port>
# def change_global(newval):
#     @global time = newval

# metodos=[lambda name,ports:ins.Instructions.create_hub(name,ports),ins.Instructions.connect_hub_hub() ]

def main():
    handler = dh.Device_handler()
    dic1 ={
        "create hub": lambda name, ports_amount :  handler.create_hub(name,ports_amount),
        "create host" : lambda args : handler.create_pc(args[0]),
        "connect" : lambda device1_name, device2_name, device1_port, device2_port : handler.setup_device_connection(device1_name, device2_name, device1_port, device2_port),
        "send" :lambda args : handler.send(args[0],args[1]),
        "disconnect":lambda device_name, device_port : handler.shutdown_device_connection(device_name, device_port)
        }
    # create parser
    parser = argparse.ArgumentParser(description="Instrucciones del script")
    parser.add_argument('-f', dest='textfile', default=True)
    args = parser.parse_args()
    filename = args.textfile
    f = open(filename, 'r')
    for line in f.readlines():
        instruction_time = 0
        codes = line.split(' ')

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
                    dic1[codes[0]+ " " + codes[1]](codes[2],ports_amount)
            
            if codes[1] == "host":
                if len(codes) == 3:
                    dic1[codes[0]+ " " + codes[1]](codes[2:])

        elif codes[0] == "connect":
            if len(codes) == 3 and codes[1].find('_') != -1 and codes[2].find('_') != -1:
                device1_name, device1_port = codes[1].split('_')
                device2_name, device2_port = codes[2].split('_')

                try:
                    device1_port = int(device1_port)
                    device2_port = int(device2_port)

                except ValueError:
                    print("Invalidad parameters")
                dic1[codes[0]](device1_name, device2_name, device1_port, device2_port)

        elif codes[0] == "disconnect":
            if len(codes) == 2 and codes[1].find('_'):
                device_name, device_port = codes[1].split('_')
                
                try:
                    device_port = int(device_port)

                except ValueError:
                    print("Invalidad parameters")
                dic1[codes[0]](device_name, device_port)
              

        
    # file2=read(f)
    # print("OO")
    # print(lines[0])

main()



