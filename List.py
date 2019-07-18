import os
import re 
import sys
from collections import OrderedDict 

class List_text(): 

    def __init__(self):
        self.parse_file_name = "Parse.txt"

    def add(self, Task, Priority = 5):
        File = open(self.parse_file_name, "a+")
        File.write("(" + Task + ")" + "(" + Priority + ")" + "(IP)\n")
        File.close()

    def new(self):
        if os.path.isfile(self.parse_file_name):
            os.remove(self.parse_file_name)

    def do(self, Num):
        if os.path.isfile(self.parse_file_name):
            with open(self.parse_file_name, "r") as File:
                Original = File.readlines()
            
            self.new()
            Task = 0
            File = open(self.parse_file_name, "a+")
            for line in Original:
                if re.search('IP', line) is not None:
                    Task += 1
                    if Task is Num:
                        completed_task = line
                    else:
                        File.write(line)
                else:
                    File.write(line)
            completed_task = completed_task.replace('IP', "C")
            File.write(completed_task)

            File.close()

    def list_tasks(self):
        if os.path.isfile(self.parse_file_name):
            File = open(self.parse_file_name, "r")
            IP_dict = {}
            P_dict = OrderedDict()
            for line in File:
                Parsed = re.split('\(|\)|\n', line)
                if(Parsed[5] == "IP"):
                    IP_dict[Parsed[1]] = Parsed[3]
                elif(Parsed[5] == "C"):
                    P_dict[Parsed[1]] = Parsed[3]
            File.close()

            print("Task(s) in Progress:")
            if len(IP_dict) is not 0:
                IP_dict = sorted(IP_dict.items(), key=lambda Item: Item[1], reverse=True)
                Num = 1
                for x in IP_dict:
                    print("    " + str(Num) +". Priority: " + x[1] + " " + " | Task: " + x[0])
                    Num += 1
            else:
                print("     There are no current tasks at the moment.")
            print("Task(s) Completed:")
            if len(P_dict) is not 0:
                for k,x in P_dict.items():
                    print("    Priority: " + x + " " + " | Task: " + k)
            else:
                print("     There are no completed tasks at the moment.")
        else:
            print("Add some task in order to see List")

def main_func(sys):
    if(len(sys.argv) is 1):
        print("Please input a valid Command:")
        print("Add")
        print("List")
        print("Do")
        print("New")
        print("Help")
    else:
        list_item = List_text()
        if(sys.argv[1] == "Add"):
            if(len(sys.argv) is not 4):
                print("Incorrect number of parameters for command - Add")
            else:
                list_item.add(sys.argv[2], sys.argv[3])
        elif(sys.argv[1] == "List"):
            if(len(sys.argv) is not 2):
                print("Incorrect number of parameters for command - List")
            else:
                list_item.list_tasks()
        elif(sys.argv[1] == "Do"):
            if(len(sys.argv) is not 3):
                print("Incorrect number of parameters for command - Do")
            else:
                list_item.do(sys.argv[2])
        elif(sys.argv[1] == "New"):
            if(len(sys.argv) is not 2):
                print("Incorrect number of parameters for command - New")
            else:
                list_item.new()
        elif(sys.argv[1] == "Help"):
            print("Add Command:")
            print("     The \"Add\" command takes in two following parameters. Task (String), Priority (Int)")
            print("     The task is encapuslated in quotations of what activity needs to be done, followed by a priority number to set the urgency of the task")
            print("List Command:")
            print("     The \"List\" command list all of the current \"In Progress\" (IP) and \"Completed\" tasks)
            print("Do Command:")
            print("     The \"Do\" command takes in one following parameter. Number (Int)")
            print("     The Number is the current IP task shown in the list")
            print("New Command:")
            print("     The \"New\" command deletes the current task list")
            print("     ")
        else:
            print("Please enter in a valid commmand, such as \"Help\" for more information")


main_func(sys)