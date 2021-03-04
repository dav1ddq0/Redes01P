import sys,argparse
import os
import parser as p
import device_handler as dh

def main():
    p.handler = dh.Device_handler()
    print(p.handler.time)
    # create parser
    parser = argparse.ArgumentParser(description="Instrucciones del script")
    parser.add_argument('-f', dest='textfile', default=True)
    args = parser.parse_args()
    filename=args.textfile
    f = open(filename, 'r')
    for line in f.readlines():
        instruction_time = 0
        line=line.replace('\n','')
        codes = line.split(' ')
        try :
            instruction_time = int(codes[0])
        except ValueError:
            print("Invalid parameter")
        codes = codes[1:]
        p.caller[codes[0]](codes[1:])

if __name__=="__main__":
    main()
