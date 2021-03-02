import sys,argparse
import os
import Instructions as ins
time=0
# <time> create hub <name> <cantidad de puertos>
# <time> create host <name>
# <time> connect <port1> <port2>
# <time> send <host> <data>
# <time> disconnect <port>

# def change_global(newval):
#     @global time = newval

# metodos=[lambda name,ports:ins.Instructions.create_hub(name,ports),ins.Instructions.connect_hub_hub() ]



dic1 ={"create hub":lambda args=ins.Instructions.create_hub(args[0],args[1]),
        "create host":lambda args=ins.Instructions.create_hub(args[0],args[1])),
        "connect":lambda args:ins.Instructions.connect_hub_hub(args[0],args[1]),
        "send" :lambda args :ins.Instructions.send(args[0],args[1]),
        "disconnect":lambda args:ins.Instructions.disconnect(args[0])}

def 
def main():
    # create parser
    
    parser =argparse.ArgumentParser(description="Instrucciones del script")
    parser.add_argument('-f', dest='textfile', default=True)
    args = parser.parse_args()
    filename=args.textfile
    f=open(filename, 'r')
    for line in f.readlines():
        codes=line.split(' ')
        time=codes[0]
        codes=codes[1:]
        if code[0]=="create":
            dic1[codes[0]]+" "+codes[1]](codes[3:])
        else:
            dic1[codes[0]](codes[2:])    

        
    # file2=read(f)
    # print("OO")
    # print(lines[0])

main()



