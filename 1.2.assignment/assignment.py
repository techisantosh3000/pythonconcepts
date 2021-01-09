a, b, c = 1, 2, 3
print(a, b, c)

#ValueError: not enough values to unpack (expected 3, got 2)
#x, y, z = 3, 4
#print(x, y, z)

m, n, _ = 2, 3, 4
print(m,_)

x = y = z = 1
print(x, y, z)
  
p = q = r = 200
print(p, q, r)  
q = 100
print(p, q, r)

x = y = [7, 8, 9] # x and y refer to the same list object just created, [7, 8, 9]
print(x)
x = [23, 20, 333]
print(x)
print(y)

#Note : it is changing the value at memory location.
x = y = [7, 8, 9] # x and y are two different names for the same list object just created, [7, 8, 9]
x[0] = 13 # we are updating the value of the list [7, 8, 9] through one of its names, x in this case
print(y) # printing the value of the list using its other name
# Output: [13, 8, 9] # hence, naturally the change is reflected


#Nested lists are also valid in python. This means that a list can contain another list as an element.
x = [1, 2, [3, 4, 5], 6, 7] # this is nested list
print  (x[0])
print  (x[1])
print  (x[2])
# Output: [3, 4, 5]
print (x[2][1])

#variables in Python do not have to stay the same type as which they were first defined -- you can simply use
#= to assign a new value to a variable, even if that value is of a different type.

a = 100
print(a)

a = "Sree Ganesha"
print(a)