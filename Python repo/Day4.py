print("Dictionaries      and        Sets")
# dictionires use hoti hai apnay data ko pair ki form mai add krna
# mtlb ke data ki koi key ho gi aur uss key ki value
# jessay name : zain iss trh name key aur zain value
# list tuples mai to ham index se call krtay thay yaha pr key se
# {}
"""info = {
    "name" : "Zain"
}
print(info["name"])
print(type(info))"""
# as same separate with comma
# typw bi print krwa sktay hai
"""info = {
    "name" : "Zain",
    "Class" : 12,
    "Age" : 17,
    "Crush" : "Emaan"
}
print(info)
print(info["Crush"])"""
# we can also store list and tuples inside the dictionary
"""info = {
    "name" : "Zain",
    "list1" : [1, 2, 3],
    "tuple1" : (1, 2, 3)
}
print(info)"""
# mutable hoti hai dictionary
# duplicae keys ni bna sktay
"""dict1 = {
    "name" : "Zain",
    "age" : 17
}
print(dict1["name"])
dict1["name"] = "Emaan"
print(dict1["name"])"""
# we can also add values and keys in dictionaries
"""info = {
    "name" : "Zain"
}
print(info["name"])
info["name"] = "Emaan"
print(info["name"])
info["age"] = 19
print(info)
print(type(info))"""
# we can also create empty dicionaries
"""info = {}
print(info)
info["name"] = "Zain"
print(info)"""
"""student = {
    "name": "Zain",
    "marks": {
        "Math": 99,
        "Chemistry": 25,
        "Physics": 33
    },
    "ages" : {
        17 : 19
    }
}
print(student)"""
# we can also create nested dictionaries
"""stud = {
    "Name" : "Zain",
    "Marks" : {
        "Math" : 99,
        "Chemistry" : 85,
        "Urdu" : 87
    },
    "Class" : 12
}
print(stud)
print(stud["Marks"]["Math"])"""
# we can also access our nested dictionary in this way
"""stud = {
    "Name" : "Zain",
    "Class" : 12,
    "Sets" : {
        12 : 19
    }
}
print(stud.keys())"""
# name.keys is used to print all the keys in the dictionaries
# yeh nested wali keys ko print ni karay ga sirf normal keys
"""stud = {
    "Name" : "Zain",
    "Class" : 17
}
print(list(stud))"""
# dictionaries ki type casting bi ki ja skti hai
# same ussi trh jessay values ki ki jati hai
"""name = {
    "name" : "Zain"
}
print(name)
print(type(name))
print(len(name))
print(list(name))
print(type(list(name)))
print(len(list(name)))"""
# iss trh type bi print krwaii ja skti hai aur length bi
"""stud = {
    "Name" : "Zain",
    "Age" : 17,
    "Class" : 12,
    "Subjects" : "Computer Science"
}

print(stud.values())"""
# name.values use hota hai dictionary ki all values print krnay ke liay
"""stud = {
    "Name" : "Zain",
    "Class" : 12,
    "Age" : 17,
    "Subjects" : ["Physics", "Math"],
    "Topic" : ("Dictionaries", ),
    "Marks" : {
        "Physics" : 85,
        "Math" : 95
    },
    "College" : "PGC"
}
print(list(stud.items()))"""
# name.item use hota hai saari keys and values ko pair ki form mai print krna as a tuple
# ham uss ki type cast bi kr sktay hai
# aur list ke andr bi kaii types save kr sktay hai
"""stud = {
    "Name" : "Zain"
}
print(stud["Name"])
print(stud.get("Name2"))"""
# agr ham get ke bagair value access krtay hai aur wo hoti ni to error ata hai
# mgr agr ham.get karay ge to agr key glt bi ho to error ni aye ga none a jaye ga
# error a jaye to yeh nuksaan hai ke error ke baad wala code run ni krta
# jab ke ,get se none a jaye ga aur baad wala code run karay ga
"""student = {
    "Name" : "Zain",
    "Age" : 17
}
print(student)
student.update({"Class" : 12})
print(student)"""
# .update use hota hai student ke andr new value print krnay ke liay as a dictionary
# iss ke liay bss {} ke andr apni dictionary add kr do
# agr update ke andr aap poorani hi key value add kr detay hai to
# uss case mai new ki jagga poorani update ho jaye gi

# set
# a collection of unordered data
# each element of set is unique and immutable
# list aur dictionary mutable hai iss wajja se inn dono ko sets mai store ni kr sktay
# {}
# dictionary ki trh sets ko bi {} se start krtay hai
# frk yeh ke uss mai data pairs mai hota sets mai ni
"""collection = {1, 2, 3, 4}
print(collection)
print(type(collection))"""
# you can also print type of set
"""sets = {1, 2, 3, "Zain", "Emaan"}
print(sets)
print(type(sets))"""
# you can also print strings and all types in set except list and dictionaries
"""sets = {1, 2, 3, 4, 2, 2, "Zain", "❤️", "Emaan", "❤️", "Zain", 2, 1}
print(sets)"""
# set ignore duplicate values and keep in mind sets are always imutable
"""collection = {1, 2, 3, 2, 3, 1, "Zain", "Emaan", "Zain"}
print(collection)
print(len(collection))"""
# agr iss ki length print krwaye ge to yeh total number print karay ga
# mgr yeh duplicates values ko count ni karay ga
"""collection = {}
print(type(collection))
coll = ()
print(type(coll))
colle = set()
print(type(colle))"""
# empty set print krnay ka tareeka thora alag hai
# dictionary tuple list ki trh ni hai
# {} () [] baaki teeno mai to ham name likh kr agay empty braces lga detay thay
# mgr yaha pr to iss ke liay koi braces hai hi i
# to iss ke liay ham set word use karay ge and () saath mai add karay ge
# khaali () use ki tp tuple ho jaye ga aur {} se dictionary
"""sets = set()
sets.add(1)
print(sets)
sets.remove(1)
print(sets)"""
# sets mai .add se add kya ja skta aur remove se remove
# 1 important point yeh ke sets mutable hai mean change kya ja skta
# mgr sets ke andr jo values hai wo immutable hai wo change ni ho skti
# agr ham koi essi cheez remove karay ge jo exist hi ni krti to error a jaye ga
"""collection = {1, 2, 3, 4}
collection.clear()
print(collection)"""
# .dot clear use hota hai set ko empty krnay ke liay
# iss ko agr use karo to sets mai jitni bi values ho jai gi wo urr jaye gi
# aur empty set return a jaye ga
"""sets = {1, 2, 3, "Zain", "❤️", "Emaan"}
sets.pop()
print(sets)"""
# .pop removes the random value
# it removes chanage value everytime the program runs
"""name = {"Zain", "Emaan"}
print(name.pop())"""
# agr issi pop ko print ke andr likhay ge to wo value print karay ge jo iss ne remove ki
"""set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.union(set2)
print(set3)"""
# .union is used to union for 2 sets and it store it in new set
"""a = {1, 2, 3}
b = {2, 3, 4}
c = a.intersection(b)
print(c)"""
# .intersection is used to find common values
"""dictionary = {
    "table" : ("a piece of furniture", "list of fact and features"),
    "cat" : "a small animal"
}
print(dictionary)"""

"""set1 = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(set1))"""

"""dictionary = {}
a = int(input("Enter marks of physics: "))
b = int(input("Enter marks of math: "))
c = int(input("Enter marks of computer: "))
dictionary.update({"Physcis" : a})
dictionary.update({"Math" : b})
dictionary.update({"Computer" : c})
print(dictionary)"""

"""set1 = {9, "9.0"}
print(set1)"""

"""username = input("Enter your username: ")
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

list1 = [a, b, c]

total = list1[0] + list1[1] + list1[2]

mx = list1[0]
if list1[1] > mx:
    mx = list1[1]
if list1[2] > mx:
    mx = list1[2]

mn = list1[0]
if list1[1] < mn:
    list1[1] = mn
if list1[2] < mn:
    list1[2] = mn

if username == username[::-1]:
    value = "Palindrome"
else:
    value = "Not Palindrome"

if username == username.isdigit():
    value1 = "Digits"
elif username == username.isalpha():
    value1 = "Alphabets"
else:
    value1 = "Mixed"

length = len(username)

if length % 2 == 0:
    value2 = "Even"
else:
    value2 = "Odd"

if length >= 6 and username[0].isupper() and any(char.isdigit() for char in username):
    value3 = "Strong Username"
else:
    value3 = "Weak Username"

tup = (mx, mn, total)

dictionary = {
    "username" : username,
    "length" : length,
    "numbers" : (a, b, c),
    "max" : mx,
    "min" : mn,
    "sum" : total
}

set1 = {9, "9.0"}

print(value)
print(value1)
print(value2)
print(value3)
print(dictionary)
print(set1)"""