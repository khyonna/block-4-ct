"""
import random

Program goals;
1. Add items to a lost (ints)
2.
3
4.

"""
import random

myList = []

def mainProgram():
    #build out while loop
    while True:
        myList = []
        print("Hello, there! :est's work with list!")
        print("Please choose from the following options. Type the number of the choice")
        choice = input("""1. Add to a list,
2. add a bunch of numbers
3.Return a value in a list, or
4.Randomsearch  )
5. linear search
6.Quit  """)
        #add a way to catch bad user responses
        if choice == "1":
            addToList()
        elif choice == "2":
            addABunch()
        elif choice == "3":
            indexValues()
        elif choice == "4":
            randomSearch()
        elif choice == "5":
            linearSearch()
            print (myList)
        else:
            break
        


def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))

def addABunch():
    print("We're gonna add a bunch of integers here!")
    numToAdd = input("How may new integers would you like to add?  ")
    numRange = input("And how zhigh would you like these numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("your lis is now complete.")
        
def randomSearch():
    print(" here to tell u right now, we dont care<33")
    myList[random.randint(0, len(myList)-1)]
def linearSearch():
    print("We're gonna check out each item one at a time in your list! this sucks.")
    searchItem = input("What you lookin for, pardner?  ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("your item is at index position {}".format(x))

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high+low) // 2
        if unique_list[mid] == x:
            print("your mother is at index position{}".fomat(mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid-1,x)
        else:
            return recursiveBinarySearch(unique_list, mid+1, high, x)
    else :
        print("your number isnt here!")

def indexValues():
    print("curious about an index position? ME TOO!")
    indexPos = input("Type an index position here:  ")
    print(myList[int(indexPos)])
            
if __name__ =="__main__":
    mainProgram()
    

    
