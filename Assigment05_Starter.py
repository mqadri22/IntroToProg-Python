# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# MQadri,2023.08.07,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
try:                                                                                # try statement to first see if the ToDoList file exists
    sourceFile = open(objFile, "r")                                                 # try opening the file with read permissions
except FileNotFoundError:                                                           # if the file is not found
    print("File 'ToDoList.txt' does not exist. Continuing without loading data")    # tell the user the file does not exist and no data is loaded
else:                                                                               # if the file is found
    for row in sourceFile:                                                          # loop through each row of data
        strData = row.split(",")                                                    # create a list object containing the elements of the row
        dicRow = {"Task": strData[0], "Priority": strData[1]}                       # assign the first element of the row contents to the Task key and the second element to the Priority key of a new dictionary object
        lstTable.append(dicRow)                                                     # append the new dictionary object as a new row of the list object containing all data
    sourceFile.close()                                                              # close the file

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("This is your current data \n")                                   # preface displayed data with message to user
        print("Task", "Priority", sep="|")                                      # provide header for forthcoming data
        for lstRow in lstTable:                                                 # for each row (dictionary) in list,
            print(lstRow["Task"].strip(),lstRow["Priority"].strip(), sep="|")   # print stripped task name and stripped
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        taskName = str(input("Enter a task: "))                                     # prompt user to enter name of a new task to include in list
        taskPriority = str(input("Enter its priority [low]/[medium]/[high]: "))     # prompt user to enter priority of a new task to include in list
        dicRow = {"Task": taskName, "Priority": taskPriority}                       # create a new dictionary object consisting of task name and priority
        lstTable.append(dicRow)                                                     # append new dictionary object as a row in existing list table
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        removedTask = str(input("What task would you like to remove? "))    # prompt user for the name of the task they want to delete
        for idx in lstTable:                                                # loop through each row of list table
            if(idx["Task"].lower() == removedTask.lower().strip()):         # if the task named by the user matches the task in the particular row
                idex = lstTable.index(idx)                                  # fetch the index (row number) of that task
                lstTable.pop(idex)                                          # delete that task and its priority from the list table
                break                                                       # exit loop upon deletion
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        targetFile = open(objFile, "w")                                                     # open file with write permissions
        for i in lstTable:                                                                  # loop through each row of list table
            targetFile.write(str(i["Task"].strip())+","+str(i["Priority"].strip())+"\n")    # write string with each task and its priority to the file
        targetFile.close()                                                                  # close the file once loop complete
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program
