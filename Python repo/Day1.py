# Day 1 of learning python with full passion and strong determination
# Python is a programming language that we will mainly use for automation in our red teaming
"""print("Python program start 😂😂")
# I will not write Hello World in my any program hehe
print("My name is Zain.", "\t My age is 17", end = "")
print("\t Today the date is 21st December 2025")
print("I am going to become a Red Teamer")
print("I will hack the World")"""

# saari lines simples hai koi essi rocket science ni just write print brackets
# then double commas ke andr jo bi likho ge wo print ho jaye ga
# \t use hota hai tapspace ke liay mean space of 8 spaces
# ab hr line ke end mai automaticcaly \n use hota hai jiss ka mtlb hota new line
# iss ko remove krnay ke liay just type kro end = " " and brackets ko khaali chorr do kuch bi type na kro
# brackets ko khaali chornay se uss mai new line ni jaye gi balkay end automatically jo new line hote wo khatam ho jaye ga
# and agr 1 hi line mai zyada likna hai to "" use kro
# spaces ka special khayaal rkhna hai
"""print("23")
print(23)
print(23 + 25)
print(50 - 23)
print(5 * 5)
print(10 / 2)"""
# agr number ko double comma mai likho ge to wo ass a string print ho ga
# double comma ke andr bss string ko likhna hai
# numbers ko +,-,*,/ bi kya ja skta hai bracket ke andr hi
# agr comma ke andr likhay ge number ko to ni ho ga kyu ke number string ni hai
# to add sub mul div comma use ni krna

# Now hmara topic hai variable
# structure variable = value hota hai iss ka
"""name = "ZAIN"
age = 17
a = 18
b = 19
print(name)
print(age)
print("My name is: ", name)
print("My age is: ", age)
age2 = age
print(age2)
c = a + b
print(c)"""
# agr to mai ne variable print krna hai to ussay name ke agay likh dena hai
# 1 rule compulsary ke agr variable string hai to double commas mai ni to essay hi
# kissi bi function ko as a variable use ni kr sktay
# variable ka 1 faida hamay baar baar value likhnay ki zaroorat ni just variable name likho
# iss ka 1 faida agr kbi value change krni prti hai to 1 hi jagga pr variable mai value change karay ge baaki hr jagga khud ba khud value change hoti jaye gi jaha jaha variable ka name ho ga
# 1 aur cheez jessay ham math mai likhtay hai a = b to iss ka mtlb hota hai a be ke equal and b a ke equal
# but python mai esssa ni hota
# python mai right side wali value assign ki jaati hai lefi side walay ko jo ke variable hota hai
# ham 1 variable ke andr hi doosray variable ko store bi kr sktay hai
# kissi variable ke andr ham koi operation bi perform krwa sktay hai
# python automatically detects the type of variable to hamay yeh btanay ki zaroorat ni ke yeh integer hai float hai ya phirr string hai hamay bss rules ko follow krna hai
"""name = "Zain"
age = 16
height = 5.9
print(name)
print(age)
print(height)
print(type(name))
print(type(age))
print(type(height))
a = type(name)
print(a)"""
# to check the type of variable write function type and then write name of variable in bracket
# you can also store it in variable then print it separatly instead of direct writing in print
"""a = 'Z'
b = "Z"
c = '''Z'''
print(a, b, c)"""
# you can write string in single double or triple comma in which you want
# mgr best option hota double mai use karo kyu ke agay ja kr bht si zarooriyat paish ati hai
"""old = False
print(old)
a = type(old)
print(a)"""
# there another type of data type that is boolean
# boolean mai sirf 2 hi cheezay hoti ya to true ya phirr false
# iss ka 1 rule hai ke True ka T aur False ka F capital hona chahiay
"""a = None
print(a)
print(type(a))"""
# 1 aur data type hai none jiss mai sirf aap ko None likh dena hota hai iss mai koi bi value ni di jati
# 1 chotti si baat python mai kuch keywords hotay hai mean reserved words
# in ko ham as a variable name use ni kr sktay jessay ke class
# in reserved words ka specifi kaam hota inn ko change ni kya jata as it is likhna prta
# wohi baat keywords ko ham identifier ni bna sktay
# identifier hota hai name chahay variable ka ho ya function ka baaki definition name se hi smj a rhi hai ke jiss se identify krwaya jaye kissi cheez ko
# case sensitive language we ji python 😂😂😂 mtlb chotta word barray word ke equal ni hota
# mean A  is  different from a
"""a = 10
b = 20
sum = a + b
print(sum)
print(a + b)
print(10 + 20)"""
# kissi bi cheez ko print krnay ke liay yeh saray tareekay valid hai
# value varibale ke andr store krwa kr print kr sktay
# variable ki jagga direct print function ke andr bi value likh sktay hai
# ya to direct value ko print ke andr add kr do sab ka result same hi hai but recomment variable wala hai

# arithmetic
"""a = 10
b = 20
sum = a + b
diff = a - b
mul = a * b
div = a / b
mod = a % b
power = a ** b
print(sum)
print(diff)
print(mul)
print(div)
print(mod)
print(power)
print(sum, diff, mod, mul, div, power)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)"""
# ** ka mean hota hai power assign krna a ** b ke mean hai a ki power b

# Relational or Comparison Operator
"""a = 50
b = 30
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)"""

#  Assigment operator
"""num = 10
#num = num + 10 # = num += 10
num += 10
print(num)
a = 10
a -= 5 # a = a - 5
print(a)
b = 5
b *= 10 # b = b * 10
print(b)
c = 10
c /= 2 # c = c / 2
print(c)
d = 10
d %= 5 # d = d % 5
print(d)
e = 10
e **= 5 # e = e ** 5
print(e)"""

# Logical operator (Only work in boolean values)
"""print(not True)
print(not False)
a = 50
b = 30
print(not (a > b))
c = True
d = True
e = False
f = False
print(c and d)
print(c and e)
print("Or operator")
print(c or d)
print(c or e)
print(e or f)
print((a > b) or (a < b))"""
# not opposites the true to false and false to true
# not can also be applied on expressions
# not operator work on one value and used by not function
# and operator works on 2 operators and used by add function
# and operator becomes true when both of given value becomes  true not in single one
# or operator also used for  2 operators by or function
# or operator becomes true when any of the given value becomes true
# it returns false only when both the values are false
# all the operators can also be applied on expressions
# yeh dekhay ge ke jo expression hai agr theek hoii to true consider karay ga aur agr glt hoi to false

# Type conversion and casting
"""a = 20
b = 10.5
c = int("10")
d = 10
add = c + d
sum = a + b # here python ne automatiically convert kr dya a jo int tha float mai
print(sum)
print(add)
print(type(c))
e = 3.144
e = str(e)
print(type(e))
print(e)"""
# string is not allowed to add in floating value
# zabardasti convert kr sktay hai aur ussko kehtay hai type  casting
# use data type jiss mai convert krna and () mai wo cheez likh do
# typecasting sirf tab kaam krti hai jab doosri type mai essa data ho jo ke convert kya ja skta hai

# Input
"""name = input("Enter your name: ")
age = int(input("Enter your age: "))
age2 = float(input("Enter your age again: "))
print("Welcome ", name)
print("Your age is: ", age)
print(type(age2), age2)
print(type(name))
print(type(age))

nm = input("Enter your name: ")
ag = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Welcome: ", nm)
print("Your age is = ", ag)
print("Your marks are: ", marks)
print(type(nm))
print(type(ag))
print(type(marks))
"""
"""a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
sum = a + b
print("Sum is =", sum)"""

"""side = float(input("Enter a side: "))

area = side * side
print(area)"""

"""a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
print("avg = ", (a + b) / 2)"""

"""a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

print(a >= b)"""

"""a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

sum = a + b + c
avg = sum / 3
print("Sum: ", sum)
print("Avg: ", avg)
print("Result: ", avg > 50)"""

"""a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

prod = a * b
S_diff = (a - b) ** 2
print("Product of given numbers is: ", prod)
print("Square difference of given numbers is: ", S_diff)"""

"""a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))

print((a > b) and (a > 0) and (b > 0))"""

"""a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))

total = a + b
print((a != b) and (total > 100))"""

"""a = float(input("Enter a number: "))

print((a % 2 == 0) and (a > 0))"""

"""a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

print(((a > 0) and (b > 0) and (c > 0)) and ((a > 50) or (b > 50) or (c > 50)))"""

"""a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

print(((a < 0) and (b < 0)) or ((a % 2 == 0) and (b % 2 == 0)))"""

"""a = float(input("Enter a number: "))

print((a % 3 == 0) and (a % 5 == 0))"""

"""a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

print((a == b) or (b == c) or (a == c))"""

"""a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))
total = a +b + c

print("All Positive: ", (a > 0) and (b > 0) and (c > 0))
print("All Negative: ", (a < 0) and (b < 0) and (c < 0))
print("At least 1 even: ", (a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0))
print("Sum > 100: ", (total > 100))
print("At least 2 equal:", (a == b) or (b == c) or (a == c))"""

"""a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

total = a + b + c
prod = a * b * c

print("Exactly 2 numbers positive: ", ((a > 0) and (b > 0) and (c <= 0)) or ((a > 0) and (c > 0) and (b <= 0)) or ((b > 0) and (c > 0) and (a <= 0)))
print("Product divisible by 2 or 5: ", (prod % 2 == 0) or (prod % 5 == 0))
print("All numbers different: ", (a != b) and (a != c) and (b != c))
print("Sum type:", (total % 2 == 0 and "Even") or "Odd")"""