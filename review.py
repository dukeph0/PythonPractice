# Print Hello World 
print("Hello world")
#indents
x = 1
if x == 1:
	# Indent to create a code block
	print("Message passed.")


# Variables and Types 
myint = 7
print(myint)
#numbers
myfloat = 7.0
print(myfloat)
myflot = float(7)
print(mylflot)
#strings
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
#using operators with strings
one = 1
two = 2
three = one + two
print(three)
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
#assignments
a, b = 3, 4
print(a,b)
# change this code
mystring = "hello"
myfloat = 10.0
myint = 20
# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)


#List, very similar to arrays
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3
# prints out 1,2,3
for x in mylist:
    print(x)
#Accessing an index
mylist = [1,2,3]
print(mylist[10])
