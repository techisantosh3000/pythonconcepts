"""
This file contains list data structure assignements.
14/01/2021

"""

# global variables.
myUniqueList = []
myLeftovers  = []

# add things to that list.
def addThingsToList(input) :
    if input in myUniqueList :
       myLeftovers.append(input)
       return False
    else :
       myUniqueList.append(input)
       return True

print(addThingsToList(100))
print(addThingsToList(100))
print(addThingsToList(200))
print(addThingsToList(300))
print(addThingsToList(400))
print(addThingsToList(500))

print(myUniqueList)
print(myLeftovers)



