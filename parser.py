import sys,argparse
import os


def main():
    # create parser
    
    # parser =argparse.ArgumentParser(description="Instrucciones del script")
    # # add a
    # parser.add_argument('filename',dest='file',required=True)
    
    # parser.add_argument('create', dest='imgFile', required=True)
    # parser.add_argument('connect', dest='scale', required=True)
    # parser.add_argument('send', dest='scale', required=True)
    # parse arguments
    # args = parser.parse_args()
    # f=args.file
    f=open("file.txt", 'r')
    lines=f.readlines()
    # file2=read(f)
    # print("OO")
    print(lines[0])

main()



