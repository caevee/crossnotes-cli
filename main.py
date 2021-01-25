#!/usr/bin/python

import sys
import requests
import json

# If no arguments are given display the help with a list of all arguments
if(len(sys.argv) == 1):
    print("Arguments:\nls = List all notes")

else:
    if(sys.argv[1] == "ls"):
        response = requests.get("https://crossnotes-api.herokuapp.com/notes")
        data = json.loads(response.text)
        for x in data:
            print("ID: " + x['id'] + "\nTitle: " + x['title'] + "\nContent: " + x['content'])
            print("")

    elif(sys.argv[1] == "rm"):
        print("Removing stuff")
    elif(sys.argv[1] == "edit"):
        print("Editing stuff")
    else:
        print("Please provide a proper argument. Open the program with no arguments to list all arguments.")
