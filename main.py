import sys, argparse
import device_handler as dh
import myParser

# dicc contains every type of error possible in connection,desconnection port
errors = {  1 : "port is busy",
            2 : "port does not exist",
            3 : "port is free"
        }
handler = dh.Device_handler()        
# dicc that func like a launcher to the principal methods
caller ={
        "hub" : lambda args:  handler.create_hub(args[0], args[1]),
        "host" : lambda args : handler.create_pc(args[0]),
        "connect" : lambda args : handler.setup_connection(args[0],args[1]),
        #"send" : lambda args : send_connect(args),
        "disconnect" : lambda args :  handler.shutdown_connection(args[0])
        }

# main :D
def main():
    
    parser = argparse.ArgumentParser(description="Instrucciones del script")
    parser.add_argument('-f', dest='textfile', default=True)
    args = parser.parse_args()
    
    filename = args.textfile
    # read input txt file
    f = open(filename, 'r')

    for line in f.readlines():
        instruction, args2 = myParser.parse(line)
        caller[instruction](args2)
        

if __name__== "__main__":
    main()
