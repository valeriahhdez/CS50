import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Please enter a number of Bitcoins")
elif sys.argv[1] == float:
    sys.exit("Please enter a valid value")

    

