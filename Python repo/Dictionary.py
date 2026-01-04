#         Python Dictionary
''' dictionary is a collection of key value pairs
in this we create and access '''
E_dict = {}  #emptu dictionary
my_msg = {"Name": "ZAIN", "Class": "12"}   #filled dictionary
print(E_dict)
print(my_msg)
#first way is to write empty dictionary and add later
#2nd way is to add data in dictionary in start
print(my_msg["Name"])
#to print particular value from tha dictionary just add tha key
#it will not print tha Name it will print tha value in the dictionary

#   Sets in Python
''' sets are the unordered
collection of uniques items'''
E_set = set() #{} is not used to prevent it to understand it dictionary
my_set = {1, 2, 3, 1, 3, 4}
# it automatically removes duplicates

print(my_set)
# all functions are same to ass list either it:
# Add
# remove etc
print(type(E_set))

#   Conditional Statements
"""
if
else
elif
nested 
"""
a = 14
v = 10

if a == v:
    print("a is equal to v")
elif a>v:
    print("a is  greater then v")
    if a>v:
        print("Greater")
elif a<v:
    print("a is  smaller then v")
else:
    print("a is not equal to b")