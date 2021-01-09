#reference : https://stackoverflow.com/questions/51252580/how-to-resolve-typeerror-can-only-concatenate-str-not-int-to-str

a = "This is a string."
b = 1000
c = 12.045

print("----------OPTION 1----------")
print("value of a is %s " % a)
print("value of b is %d " % b)
print("value of c is %f " % c)


print("-----------OPTION 2---------")
print("value of a is  ", a)
print("value of b is  ", b)
print("value of c is  ", c)
