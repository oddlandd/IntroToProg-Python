# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KOdland, 5.16.2020, Added file processing, adding new tasks, printing list, saving list
# KOdland, 5.17.2020, Added code to remove a task
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # A Capture the user option selection
lstRow = []  # a row of data from the file
strTask = ""  # user input of a new task
strPriority = "" # user input of priority for the task

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
loadFile = open(objFile, "r")
for row in loadFile:
    lstRow = row.split(",")  # returns a list with data from each line of file
    dicRow = {"Task":lstRow[0], "Priority":lstRow[1]}
    lstTable.append(dicRow)
loadFile.close()

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
        print("Your current to-do items are:")
        print("Task | Priority")
        for row in lstTable:
            print(row["Task"] + " | " + row["Priority"].strip())
        input("\nPress enter to continue")  # pauses for user input, so they can see the list
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a Task: ")
        strPriority = input("Enter a Priority: ")
        dicRow = {"Task":strTask, "Priority":strPriority + "\n"}  # make a dictionary with user inputs
        lstTable.append(dicRow)  # add the dictionary to the table of data
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        removeCounter = False
        strRemove = input("Please type in the task you'd like to remove: ")
        for row in lstTable:
            if row["Task"].lower() == strRemove.lower():  # if the task in the dictionary matches the task to remove
                lstTable.remove(row)  # remove the row from the table
                removeCounter = True  # switch the counter to show that an item was removed
                break
        if not removeCounter:
            print("Your task was not on the list!")
        else:
            print("You removed this task")
        input("\nPress enter to continue")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        openFile = open(objFile, "w")
        for row in lstTable:
            openFile.write(row["Task"] + "," + row["Priority"])
        openFile.close()
        print("Task/Priority data saved to file")
        input("\nPress enter to continue")
        continue
        
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
