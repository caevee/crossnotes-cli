#!/usr/bin/python

import sys
import requests
import json

# If no arguments are given display the help with a list of all arguments
if(len(sys.argv) == 1):
    print("Arguments:\nls = List all notes")

else:
    # Code to run when argument happens to be ls(list)
    if(sys.argv[1] == "ls"):
        # Send api get requests and get all the data
        response = requests.get("https://crossnotes-api.herokuapp.com/notes")
        # Convert data into python data structure
        data = json.loads(response.text)
        # Print array of data
        for x in data:
            print("ID: " + x['id'] + "\nTitle: " + x['title'] + "\nContent: " + x['content'])
            print("")

    # Code to run when argument happens to be add
    elif(sys.argv[1] == "add"):
        # Set default data and a variable that prevents the api call if data couldnt be set due to insufficient arguments
        data = {}
        dataSet = False
        # Try to set data. Will cancel out if arguments are not sufficient
        try:
            data = {"title": sys.argv[2], "content": sys.argv[3]}
            dataSet = True
        except:
            print("Please provide a proper set of arguments")

        # Now if data is all set we send it out to the api
        if (dataSet):
            # This try/except just in case the api itsself breaks
            try:
                response = requests.post("https://crossnotes-api.herokuapp.com/notes", data=data)
            except:
                print("An error occured")

    # Code to run when argument happens to be rm(remove)
    elif(sys.argv[1] == "rm"):
        id = 0
        try:
            id = sys.argv[2]
        except:
            print("Please provide a proper set of arguments")


        if(id != 0):
            # This try/except just in case the api itsself breaks
            try:
                response = requests.delete(f"https://crossnotes-api.herokuapp.com/notes/{id}")
            except:
                print("An error occured")



    # Code to run when argument happens to be edit
    elif(sys.argv[1] == "edit"):
        """ All this doesn't work for some reason.. gonna try and fix later
        # Set default data and a variable that prevents the api call if data couldnt be set due to insufficient arguments
        id = 0
        data = {}
        dataSet = False
        # Try to set data. Will cancel out if arguments are not sufficient
        try:
            id = {sys.argv[2]}
            data = {"title": sys.argv[3], "content": sys.argv[4]}
            dataSet = True
        except:
            print("Please provide a proper set of arguments")

        # Now if data is all set we send it out to the api
        if (dataSet and id != 0):
            # This try/except just in case the api itsself breaks
            try:
                response = requests.patch(f"https://crossnotes-api.herokuapp.com/notes/{id}", data=data)
            except:
                print("An error occured")
        """
    # Code to run when argument is not listed
    else:
        print("Please provide a proper argument. Open the program with no arguments to list all arguments.")
