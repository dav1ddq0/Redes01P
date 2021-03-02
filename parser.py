import sys,argparse
import os


def main():
    # create parser
    
    parser =argparse.ArgummentParser(description="Instrucciones del script")
    # add a
    parser.add_argument(, dest='file')
    
    # parser.add_argument('create', dest='imgFile', required=True)
    # parser.add_argument('connect', dest='scale', required=True)
    # parser.add_argument('send', dest='scale', required=True)
    # parse arguments
    args = parser.parse_args()
    f=args.file
    inst=open(f, 'r')
    print(ins[0])




