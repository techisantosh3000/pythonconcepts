"""
This file contains if-statement assignment.

"""
#Create a function that accepts 3 parameters and checks for equality between any two of them.
def myFunction(a,b,c):
    if a == b:
        return True
    elif b == c:
        return True
    else :
        return False

print(myFunction(1,2,2))

print(myFunction(1,"3",3))

#Extra Credit:
def myModifiedFunction(a,b,c):
    if int(a) == int(b):
        return True
    elif int(b) == int(c):
        return True
    else :
        return False

print(myModifiedFunction(6,5,"5"))        


