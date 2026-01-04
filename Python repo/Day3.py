# list and tuples:
# list is used to store set of values
# can store every type of data
#[]
# used to store multiple data in single place
"""marks1 = 94.2
marks2 = 95
marks3 = 95.5
marks4 = 100
marks5 = 80

print(marks1, marks2, marks3, marks4, marks5)
print(marks1)
print(marks2)
print(marks3)
print(marks4)
print(marks5)"""
from Tools.scripts.var_access_benchmark import make_nonlocal_reader
from re import A

# ab yeh agr zyada data ho to baar baar variable likhna in ko track krna bht bht zyada mushkil ho jata
# to iss sab se bachnay ke liay ham 1 hi list mai issay save kr letay hai
# variable name = and [] mai saari values
# int float string hr cheez store ki ja skti hai
"""marks = [90 , 20, 30, 40, 50]
print(marks)
print(type(marks))
print(marks[0])"""
# agr koi specific value print krni ho to index number likh do same as string
"""marks = [10, 20, 30, 40, 50]
print(marks)
marks[0] = "Zain"
print(marks[0])
print(marks[1])
print(marks[2])
print(len(marks))"""
# string aur list mai main difference string change ni ki ja skti mean immutable
# lists are mutable ham change kr sktay aur poori value ka index hota iss mai
# ham list ke andr string save bi kr sktay
"""details = ["Zain", 17,  "Sialkot"]
print(details)
details[0] = "Emaan"
details[1] = 19
details[2] = "Karachi"
print(details)"""
# strings mai index pr value ko access krna allow bss
# mgr list mai ham access bi  kr sktay change bi kr sktay
# as same as string yeh hamay error de ga agr wo index dallay ge jo exist ni krta
# list slicing is also possible
"""marks = [10, 20, 30, 40, 51]
print(marks[0 : 2])
print(marks[ : 3])
print(marks[0 : len(marks)])
print(marks[0 : ])"""
# same rules as string
# it also have negative index same as string
"""marks = [1, 2, 3]
marks.append(4)
print(marks)"""
#list.append is used to attch the value in last of list that we will write in brackets
"""marks = [1, 2, 5, 10, 3, 9, 4,6, 8, 7]
marks.sort()
print(marks)"""
# list.sort use to arrange it in accending order
# sort value return ni krta issay essay hi likh do ya  alag print bnao ni to none aye ga
"""marks = [2, 1, 3, 5, 4]
marks.sort(reverse = True)
print(marks)"""
# to print in descending order just write reverse = True in brackets()
"""name = ["Zain", "Naveed", "Emaan", "Fatima"]
name.sort()
print(name)"""
# sorting is appicable in everything int strings etc
"""name = ["Zain", "Emaan", "Naveed", "Fatima"]
name.sort(reverse = True)
print(name)"""
"""number = [1, 2, 3, 5]
number.reverse()
print(number)"""
# . reverse saari tarteeb change kr deta hai
"""name = ["Zain", "Emaan"]
print(name)
name.insert(0, "Emaan")
name.insert(1, "Fatima")
print(name)"""
# insert ke ke index number lgao aur uss index pr kya add krna wo lgao
# baaki values khud ba khud 1 number agay ho jaye gi
# append end mai add krta hai aur index particular index pr
"""name = [1, 2, "ZAiN", 5]
name.remove(1)
print(name)"""
# remove is used to remove tha value in list it removes by value not by index
"""name = ["Zain", 1, "Emaan", 2]
name.pop(1)
print(name)"""
# pop remove the element by variable
# issay frk ni prti variable ke type se

# Tuples
# immutable
# ()
# value assign ni ki ja skti just like string
"""tup = (1, 2, 3)
print(type(tup))
print(tup)"""
# tareeka list se same hai
# just [] ki jagga () use hoti hai
"""tup = (1, 2, 3, 4)
print(tup[1])"""
# tuples can also be accesses by their index
# tuples mai ham value assign ni kr sktay kissi index ko
# tup[0] = 1 this type of assigment not allowed
"""tup = ()
print(type(tup))
print(tup)"""
# to create empty tuple just ()
"""tup = (1, )
print(tup)"""
# agr single tuple add krna hai to best tareeka hai ussay comma se separate lazmi kro
# agr comma ni lagaye ge to wo issay tuple consider ni kray ga balkay integar consider karay ga
# last mai comma lgana optional hai mgr 1 ho to lazmi hai
"""tup = (1, 2, 3, 4, 5, 6, 7)
print(tup[1 : 5])"""
# slicing of tuple is same as list
"""tup = (1, 2, 1, 3)
tup = tup.index(1)
print(tup)"""
# index is used to find the index number of any thing
# mgr agr 1 2 baar hai andr to yeh bss pehla consider karay ga
"""tup = (1, 2, 3, 4, 1, 1)
tup = tup.count(1)
print(tup)"""
# .count use hota hai kissi bi value ki occurance count krnay ke liay
# important baat list jo thi wo kuch return ni thi krti none a jata tha agr ussay print mai likhay token
# mgr iss mai essa ni hai issay ussi variable ke andr store krna prta hai ya print mai likh do

"""a = input("Enter your 1st favorite movie name: ")
b = input("Enter your 2nd favorite movie name: ")
c = input("Enter your 3rd favorite movie name: ")

movies  = [a, b, c]
print(movies)"""
# or
"""movies  = []

a = input("Enter your 1st favorite movie name: ")
b = input("Enter your 2nd favorite movie name: ")
c = input("Enter your 3rd favorite movie name: ")

movies.append(a)
movies.append(b)
movies.append(c)
print(movies)
"""
# upper walay dono tareekay theek hai

"""list1 = [1, 2, 3, 2, 1]
if list1 == list1[ :: -1]:
    print("pa")"""
# or
"""list1 = [1, 2, 3, 2, 1]
a = list1.copy()
a.reverse()
if list1 == a:
    print("pa")"""
# in this case also both methods are true

"""tup = ("C", "D", "A", "A", "B", "B", "A")
print(tup.count("A"))"""

"""lis1 = ["C", "D", "A", "A", "B", "B", "A"]
lis1.sort()
print(lis1)"""

"""a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

list1 = [a, b, c]
print(list1)
print(len(list1))
print(list1[0], list1[-1])"""

"""lis1 = [10, 20, 30, 40, 50]
lis1.pop(-1)
lis1.insert(2, 25)
print(lis1)"""

"""list1 = []

list1.append(int(input("Enter 1st number: ")))
list1.append(int(input("Enter 2nd number: ")))
list1.append(int(input("Enter 3rd number: ")))
list1.append(int(input("Enter 4th number: ")))
list1.append(int(input("Enter 5th number: ")))

print(list1)

list1.reverse()

print(list1)"""

"""a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))
e = int(input("Enter 5th number: "))

values = [a, b, c, d, e]

mx = values[0]
if values[1] > mx:
    mx = values[1]
if values[2] > mx:
    mx = values[2]
if values[3] > mx:
    mx = values[3]
if values[4] > mx:
    mx = values[4]

mn = values[0]
if values[1] < mn:
    mn = values[1]
if values[2] < mn:
    mn = values[2]
if values[3] < mn:
    mn = values[3]
if values[4] < mn:
    mn = values[4]
total = values[0] + values[1] + values[2] + values[3] + values[4]

print(f"Maximum value is {mx}")
print(f"Minimum value is {mn}")
print(f"Sum is {total}")"""

"""string = input("Enter a string: ")
if string == string[ :: -1]:
    print("String is Palindrome")
else:
    print("Not Palindrome")

if string.isalpha():
    print("Alphabets")
elif string.isdigit():
    print("Numbers")
else:
    print("Mixed")

a = len(string)

if a % 2 == 0:
    print("Even")
else:
    print("Odd")

if (a >= 6 and string[0].isupper() and any(char.isdigit() for char in string)):
    print("Strong String")
else:
    print("Weak")"""
# any is used to check any condition in string