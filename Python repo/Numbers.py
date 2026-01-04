#            Numbers in Python
x = 10    # int
y = 5.7   # float
z = 2 +3j #complex
print(x,y,z)

#          String formatting
str1 = 'Zain'

str2 = "ZAIN"

str3 = '''Multi
line
string'''
print(str1)
print(str2)
print(str3)

#      Boolean Data Type
'''Booleans have only two type of date
True
False'''
'''
a = True
b = False
'''
# boolean is used in and or not operators
a = True
b = False
result = a and b  # output is false

a = True
b = False
result = a or b # output is True
'''
a = True
b = False
result = not a # output is False'''

#         Tuples in Python
''' Tuples is a datatype that store data in sequence
immutable sequence
data cannot be modified'''

my_tuple = (1, 2, 3)

my_tuples = 1, 2, 3

single_line_tuple = (5,)

print(my_tuple)
print(my_tuples)
print(single_line_tuple)

#     Python list
Elist = []  #empty list
mylist = [1, 2, 3, "ZAIN"] #with elements of any data type
#string should be written in double commas
#it is used to store data in sequence in the way of list

# to access elements
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
''' 0 is used for 1st one
no matter 1st one value is 0 or 1'''

#slicing list
print(mylist[1:3])
'''to print tha some part of list
write 1st and 2nd name and use : between them'''
print(Elist)
# list is empty so it  will print nothing

print(mylist)
#to print whole list just write tha list name

zlist = [1, 2, 3, 4, "ZAIN", 5]
print(zlist)

xlist = [1, 2, 3, 4, "ZAIN"]
xlist.insert(1, "NAVEED") #insert is a function to insert data in any place
print(xlist)
'''in insert we first insert tha data on particular data
tha other data will be automatically moved to next one automatically'''
ylist = [1, 2, 3, 4, "ZAIN"]
'''
ylist.extend(5, 6, 7, 8)
it will give error on adding multipe values 
to add multiple values add in variable then print
'''
add = 5, 6, 7, 8
ylist.extend(add) #EXTEND IS A FUNCTION TO EXTEND A LIST
print(ylist)
# in extend you can add data in last, but it takes one value so add value
#1st add in variable
#then print variable in extend
#then it will print multiple data

# now how to remove data from list
newlist = [1, 2, 3, "Python"]
newlist.remove("Python") #remove is a function to remove particular value from list
print(newlist)

nwlist = [1, 2, 3, "Python"]
nwlist.pop(2) #pop is a function to remove particular value from list on the bahalf of its index
print(nwlist)

nelist = [1, 2, 3, "Python"]
nelist.clear() #clear is a function to remove whole list
print(nelist)