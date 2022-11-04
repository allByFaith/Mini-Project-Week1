# This is the mini-project
# File Name     : miniProjectWeek1.py
# Date          : 21 Oct 2022
# Programmer    : Samuel KO
# Description   : Build a Product Menu for
#               : 1) Product menu
#               : 2) Add Product menu
#               : 3) Update product menu
#               : 4) Delete product menu
#               : 0) Return to Main Menu

# Set the global myProdList as global variable by 
# putting it to listStorage.py file, then import it
import listStorage

def productMenu():

    # create a product list with 8 items for testing
    # myProdList = ['def', 'efg', 'ijk', 'lmn', 'opq', 'rst', 'wuv', 'xyz']

    prodKeepOn = True

    while prodKeepOn:
            print("___________________________")
            print("_ Product Menu            _")
            print("_                         _")
            print("_ 1)--Retrieve Product    _")
            print("_ 2)--Add New Product     _")
            print("_ 3)--Update Product      _")
            print("_ 4)--Delete Product      _")
            print("_ 0)--Return to Main Menu _")
            print("_                         _")
            print("___________________________")

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
                        print("Good, you want to exit product menu.")
                        prodKeepOn = False
                    elif (choice == 1):
                        if (len(listStorage.myProdList) == 0):
                            # productMenu()
                            print("You have no item in your product list!")
                        else:
                            print("current product item in your list : ", listStorage.myProdList)
                    elif (choice == 2):
                        # print(len(myProdList))
                        inputItem = input("Enter product : ")
                        listStorage.myProdList.append(inputItem)
                        print("List after input the item : ", listStorage.myProdList)
                    elif (choice == 3):
                        inputItem = input("Enter the name of product that you want to update: ")
                        itemToUpdate = input("What you want to update: ")
                        listStorage.myProdList[listStorage.myProdList.index(inputItem)] = itemToUpdate
                        print(f"Updated! the product {inputItem} has been updated to {itemToUpdate}!")
                    elif (choice == 4):
                        wantToRemoveItem = input("Enter the product that you want to delete: ")
                        print("the want to delete item", wantToRemoveItem)
                        print(f"Before delete -->{listStorage.myProdList}")
                        count = len(listStorage.myProdList)
                        for x in listStorage.myProdList:
                            if (x == wantToRemoveItem):
                                listStorage.myProdList.remove(x)
                                print(f"Deleted! the product {wantToRemoveItem} has been deteleted!")
                            elif(count == 1):
                                print("Delete item not found, check your product again!")
                            count -= 1
                else:
                    print("Input a wrong selection, try input again!")
                    continue
            except:
                print(f"Invalid choice --> {choice}")
                continue
