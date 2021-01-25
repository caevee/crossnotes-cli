#!/usr/bin/python

import sys
import requests
import json

# If no arguments are given display the help with a list of all arguments
if(len(sys.argv) == 1):
    print("Display help")

else:
    if(sys.argv[1] == "ls"):
        print("Listing stuff")
        try:
            print(sys.argv[2])
        except:
            response = requests.get("https://crossnotes-api.herokuapp.com/notes")
            data = json.loads(response.text)
            print(data)

    elif(sys.argv[1] == "rm"):
        print("Removing stuff")
    elif(sys.argv[1] == "edit"):
        print("Editing stuff")
    else:
        print("Please provide a proper argument. Open the program with no arguments to list all arguments.")
