# This is the mini-project
# File Name     : mainMenu.py
# Date          : 22 Oct 2022
# Programmer    : Samuel KO
# Description   : Build a Main Menu
#               : 1) Go to product menu
#               : 0) Exit the entire app/system

import sys
import os
import listStorage

# from productMenu import *
#global myProdList
from productMenu import *
from orderMenu import *

def mainMenu():
    keepOn = True

    while keepOn:
            print("_________________________")
            print("_ Welcome to CLI system _")
            print("_                       _")
            print("_  1)--Product Menu     _")
            print("_  2)--Order Menu       _")
            print("_  0)--Exit System      _")
            print("_________________________")
            print(" ")
            try:
                choice = input("Please enter your choice :- ")
                if (choice.isdigit()):
                    choice = int(choice)
                    pass
                else:
                    print("Oops, wrong input of \'" + choice + "\' !!!!")
                    continue

                if choice in range(0, 3):
                    if (choice == 0):
                        print("Good, you want to exit the system, see you next time~")
                        keepOn = False
                    elif (choice == 1):
                         productMenu()
                    elif (choice == 2):
                         orderMenu()
                else:
                    print("Input a wrong selection, try input again!")
                    continue
            except:
                print(f"Invalid choice --> {choice}")
                continue
mainMenu()