import os   

tableSize = int(input("Enter the size of Hash Table:"))

 # to clear terminal after every iteration
def clear():
    try:
        os.system("cls")
    except:
        os.system("clear")


def menu1():
    print("\n=======Menu========")
    print("1. Linear probing")
    print("2. Chaining without replacement")
    print("3. Exit")
    _ = int(input("Select a Collision Handeling method:"))
    return _


def menu2():
    print("\n=======Menu========")
    print("1. Insert an element")
    print("2. Search an element")
    print("3. Display the Table")
    print("4. Change collision handeling method")
    _ = int(input("Enter your Choice:"))
    return _


# Functions for Linear probing

def insertL():
    name = input("Enter the name:")
    number = input("Ente the Number:")
    row = name + ":" + number
    position = int(number)%tableSize
    
    if(hashTable[position]==None):
        hashTable[position] = row
    else:
        # Here collision occured
        print(f"Collision occured for {name}")
        while hashTable[position]!=None:
            position+=1
            if position>=tableSize:
                position = 0

        hashTable[position] = row
        
        
def searchL():
    _ = [range(len(hashTable))]
    name = input("Enter the name:")
    number = input("Enter the number:")
    count = 0
    for i in range(len(hashTable)):
        count +=1
        if hashTable[i] is not None:
            _ = hashTable[i].split(":")
            if _[0] == name and _[1] == number:   
                print(f"{name} found at {i} and Comparisons required are {count}")
                return
    else:
        print("Not found")
        
        
def displayL():
    _ = [range(len(hashTable))]
    for i in hashTable:
        if i is None:
            print("Name : None  ||  Number : None")
        else:
            _ = i.strip(":")
            print(f"Name : {_[0]}   ||  Number : {_[2]}")
        
        

        
def insertC(hashTable):
    name = input("Enter the name:")
    number = input("Ente the Number:")
    row = name + ":" + number
    key = hashing(int(number))
    hashTable[key].append(row)
        
def displayC(hashTable):
    for i in range(len(hashTable)):
        print(i, end = " : ")
        for j in hashTable[i]:
            print(j)
        print()


def searchC(hashTable):        
   count = 0
   _ = [range(len(hashTable))]
   name = input("Enter the Name:")   
   number = input("Enter the Number:")
   for i in range(len(hashTable)):
       for j in hashTable[i]:
           count += 1
           if j==None:
               count += 1
           if j!=None:
               _ = j.split(":")
               if _[0] == name and _[1] == number:
                   print(f"{name} found at position {i} and the Comparisions required are {count-1}")
       count += 1
        
if __name__ == "__main__":
    run = True
    choice1 = 0
    while run:
        choice1 = menu1()
       
        if choice1 == 1:
            clear()
            on = True
            choice2 = 0
            # Initialize the hash table with null elements
            hashTable = list(None for i in range(tableSize))
            while on:
                choice2 = menu2()
                if choice2 == 1:
                    insertL()
                elif choice2 == 2:
                    searchL()
                elif choice2 == 3:
                    displayL()
                elif choice2 == 4:
                    on = False
                else:
                    print("Invalid Choice")
                    continue

        elif choice1 == 2:
            clear()
            on = True
            choice2 = 0
            hashTable = [[] for _ in range(tableSize)]
            def hashing(key):
                return key % len(hashTable)
            while on:
                choice2 = menu2()
                if choice2 == 1:
                    insertC(hashTable)
                elif choice2 == 2:
                    searchC(hashTable)
                elif choice2 == 3:
                    displayC(hashTable)
                elif choice2 == 4:
                    on = False
                else:
                    print("Invalid Choice")
                    continue
        elif choice1 == 3:
            run = False
            exit(0)
        else:
            print("Invalid choice!")
            continue
