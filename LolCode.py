from Interp import LOLCodeInterpreter
from Parser import parser
import argparse

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='LolCode interpretator')
    arg_parser.add_argument('-f', nargs=1, help='input filename')
    args = arg_parser.parse_args()
    filename = args.f[0]
    with open(filename, 'r') as f:
       data = f.read()
       if data:
                try:
                   tree = parser.parse(data)
                   interpret = LOLCodeInterpreter(tree)
                   interpret.execute_program()
                except Exception as e:
                    print(e)