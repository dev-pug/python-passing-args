import sys
import getopt

def getArgs(argv):
    arg_input = ""
    arg_output = ""
    arg_user = ""

    try:
        opts, args = getopt.getopt(argv[1:], "hi:u:o:", ["help", "input=", "user=", "output="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-i", "--input"):
            arg_input = arg
        elif opt in ("-u", "--user"):
            arg_user = arg
        elif opt in ("-o", "--output"):
            arg_output = arg

    print("input:", arg_input)
    print("user:", arg_user)
    print("output:", arg_output)

def usage():
    arg_help = "-i <input> -u <user> -o <output>"
    print(arg_help)

if __name__ == "__main__":
    getArgs(sys.argv)