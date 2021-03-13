import sys, argparse
import device_handler as dh
import myParser


handler = dh.Device_handler()        
# dicc that func like a launcher to the principal methods
caller ={
        "hub" : lambda args:  handler.create_hub(args[0], args[1], args[2]),
        "host" : lambda args : handler.create_pc(args[0], args[1]),
        "connect": lambda args : handler.setup_connection(args[0],args[1], args[2]),
        "send": lambda args : handler.send(args[0], args[1], args[2]),
        "disconnect": lambda args :  handler.shutdown_connection(args[0], args[1])
        }

# main :D
def main():
    
    # parser = argparse.ArgumentParser(description="Instrucciones del script")
    # parser.add_argument('-f', dest='textfile', default=True)
    # args = parser.parse_args()
    #
    # filename = args.textfile
    filename = input()
    # read input txt file
    f = open(filename, 'r')

    for line in f.readlines():
        try:
            instruction, args2 = myParser.parse(line)
        except ValueError:
            print("Parse Error wrong line sintax")
            return
        # try:
        caller[instruction](args2)
        # except ValueError:
        #     print("Excution Error")
        #     return

    handler.finished_network_transmission()
    
if __name__== "__main__":
    main()
