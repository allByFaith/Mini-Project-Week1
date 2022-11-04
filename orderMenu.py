# This is the mini-project
# File Name     : orderMenu.py
# Date          : 22 Oct 2022
# Programmer    : Samuel KO
# Description   : Build a Order Menu
#               : 1) Print order
#               : 2) Add order
#               : 3) Update order
#               : 4) Delete order
#               : 0) Exit Order Menu

import sys
import os

# Set the global myProdList as global variable by 
# putting it to listStorage.py file, then import it
import listStorage

def orderMenu():
    keepOn = True

    while keepOn:
            print("_________________________")
            print("_ Order Menu            _")
            print("_                       _")
            print("_ 1)--Print Order       _")
            print("_ 2)--Add Order         _")
            print("_ 3)--Update Order      _")
            print("_ 4)--Delete Order      _")
            print("_ 0)--Exit Order menu   _")
            print("_                       _")
            print("_________________________")
            try:
                choice = input("Please enter your choice :- ")
                if (choice.isdigit()):
                    choice = int(choice)
                    pass
                else:
                    print("Oops, wrong input of \'" + choice + "\' !!!!")
                    continue
                    
                if choice in range(0, 5):
                    if (choice == 0):
                        print("Good, you want to exit order menu.")
                        keepOn = False
                    elif (choice == 1):
                         # Print order
                         print("Print Order")
                    elif (choice == 2):
                        print("Add Order")
                    elif (choice == 3):
                        print("Update Order")
                    elif (choice == 4):
                        print("Delete Order")
                else:
                    print("Input a wrong selection, try input again!")
                    continue
            except:
                print(f"Invalid choice --> {choice}")
                continue