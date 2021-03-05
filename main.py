import sys, argparse
import device_handler as dh
import myParser

def main():
    
    handler = dh.Device_handler()
    parser = argparse.ArgumentParser(description="Instrucciones del script")
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
        caller[instruction](args2)
        

if __name__== "__main__":
    main()
