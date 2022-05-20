import json
import sys,getopt

def main(argv):
    server=""
    portal="My default portal"
    razorize=""
    verbose=True

    def help():
        print('Usage: hey -s SERVER [-p PORTAL] -r [-v] [-h]')
        print('dkgjjgkjgkjg kfgjdkfjgk dfkgd kfkgjkgj')
        print('   -s, --server		Mandatory. my BIG server')
        print('   -p, --portal		my small portal')
        print('   -r, --razorize		Mandatory. whether razorizer or let it be')
        print('   -v, --verbose		verbosion mode god')
        print('   -h, --help		Display help and exit')
    try:
        opts, args = getopt.getopt(argv,"s:p:rv",["server=","portal="])
    except getopt.GetoptError:
        help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
            sys.exit()
        elif opt in ("-s", "--server"):
         server = arg
        elif opt in ("-p", "--portal"):
         portal = arg
        elif opt in ("-r", "--razorize"):
         razorize = arg
        elif opt in ("-v", "--verbose"):
         verbose = arg

    if server == "":
        print("Missing parameter server")
        help()
        sys.exit(2)
    elif razorize == "":
        print("Missing parameter razorize")
        help()
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
