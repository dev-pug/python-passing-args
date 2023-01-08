import sys
import argparse

def getArgs(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", help="specify the user")
    parser.add_argument("-i", "--input", help="specify the input file")
    parser.add_argument("-o", "--output", help="specify the output file")
    args = parser.parse_args()
    printArgs(args)

def printArgs(args):
    print("input:", args.input)
    print("user:", args.user)
    print("output:", args.output)

if __name__ == "__main__":
    getArgs(sys.argv) 