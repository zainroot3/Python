# Revision of the Day 1:

"""a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

print("At least 1 number is 0: ", ((a == 0) and "1st value is 0") or ((b == 0) and "2nd value is 0") or ((c == 0) and "3rd value is 0"))
print("All numbers are non 0: ", (a != 0) and (b != 0) and (c != 0))
print("Only 1 number is negative: ", ((a < 0) and (b >= 0) and (c >= 0)) or ((b < 0) and (c >= 0) and (a >= 0)) or ((c < 0) and (a >= 0) and  (b >= 0)))
print("None is negative: ", (a >= 0) and (b >= 0) and (c >= 0))"""

"""a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

total = a + b + c

print("Only one middle number: ",
      ((((a > b) and (a < c)) or ((a > c) and (a < b))) and "1st value is middle") or
      ((((b > a) and (b < c)) or ((b < a) and (b > c))) and "2nd value is middle") or
      ((((c > a) and (c < b)) or ((c < a) and (c > b))) and "3rd value is middle") or
      "No middle value"
      )

print("Exactly one number is Even: ",
      ((a % 2 == 0) and (b % 2 != 0) and (c % 2 != 0) and f"{a} is Even") or
      ((b % 2 == 0) and (a % 2 != 0) and (c % 2 != 0) and f"{b} is Even") or
      ((c % 2 == 0) and (a % 2 != 0) and (b % 2 != 0) and f"{c} is Even") or
      "Only one value is not Even"
      )

print("Sum is more then 50", total > 50)"""

# Now day 2 started from here
# Strings and Conditional Statements

"""a = 'String 1'
b = "String 2"
 c = String 3 

print(a, b, c)"""
# string is recommended in singlue quotes
# kyu ke agr aap ko string ke andr quotes use krni ho to python confuse ho jata
# and triple quotes for multiple line same rule as comments
# example se quotes iss liay remove kiyeb takkay comment mai issue na aye
"""a = This is a multiple line string 
hrhrhrhrhhhrhrh"""
"""b = "I am \n Zain"
c = "This is \t string"
print(a)
print(b)
print(c)"""
# \n for new line and \t for tab space
"""str1 = "Zain"
len1 = len(str1)
str2 = "Naveed"
len2 = len(str2)
final_str = str1 + " " + str2
print(final_str)
print(len1)
print(len2)
print(len(final_str))"""
# string count space as a value
"""a = "Zain ul Abdeen"
print(a[1])"""
#string ka name and index number
"""a = "Zain Z"
print(len(a))
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])"""
# important thing in string we can just access index cannot replace
# slicing hota hai string ko part mai torna
# string name and starting and ending index
# starting index hamesha included hota hai mgr ending index ni
"""a = "Zain Naveed"
print(a[0 : 4])"""
# if starting index not written it consider as 0
# if ending not entered then it consider is at len(str) mean last
"""a = "Zain"
print(a[ : 2])
print(a[1 : ])"""
"""a = "Zain"
print(a[0 : len(a)])"""
# python also have negative indexing feature
"""a = "Zain"
print(a[-4 : ])"""
"""a = "Zain"
print(a.endswith("Z"))"""
# str.endswith is used to check end of string
# agr end match ho jaye to true ni to false
"""a = "zain"
print(a.capitalize())"""
# str.capitalize is used to capitalize tha 1st letter of string
# yeh sirf waha capital jaha capitalize use kya original mai ni
# agr original mai use krna hai to aap alag variable mai store kr lo jessay ya ussi mai kr lo
"""a = "zain"
a = a.capitalize()
b = a.capitalize()
print(b)
print(a)"""
"""a = "Zain"
print(a.replace("Z", "A"))"""
# str.replace is used to replace old value to new
# pehlay old value likhni then new
"""a = "Zain"
print(a.find("Zain"))"""
# yeh jo hai na aap ke search keyword ka pehlay name ka index number bta de ga jaha se start hota hai
# agr aap essi cheez ke liay search kro jo exist ni krti to -1 a jaye ga
"""a = "My name is Zain and heheheheheheh"
print(a.count("h"))"""
# count use hota hai koi letter ya word count krnay ke liay
"""a = input("Enter your name: ")
print("Length of your name is: ",  len(a))"""
"""a = "I am $ and i willbe $$$$ many tume hahah $$$"
print(a.count("$"))"""
"""age = 19

if age >= 18:
    print("You ara applicable for licenses")
else:
    print("You cannot drive")"""
"""light = "Red"
if light == "Green":
    print("You can go")
elif light == "Red":
    print("Stop")
elif light == "Yellow":
    print("Wait")
else:
    print("Light is broken")"""
# elif only run when if become false
# 4 space(tab) ko intendation kehtay hai

"""marks = float(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80 and marks < 90:
    print("Grade B")
elif 90 > marks >= 70:
    print("Grade C")
elif marks < 70:
    print("Grade D")
else:
    print("Fail")"""
# elif 2 wala tareeka aur baaki tareekay dono theek hai
"""age = 14
if age >= 18:
    if age >= 80:
        print("You are old")
    else:
        print("Can drive")
else:
    print("Stop")"""
# nested is use to use condition in another conditon
"""a = int(input("Enter a number: "))
if a % 2 == 0:
    print("Even")
else:
    print("Odd")"""

"""a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a > b and a > c:
    print(f"{a} is greater")
elif b > a and b > c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")"""

"""a = int(input("Enter a number: "))
if a % 7 == 0:
    print("Number is divisible by 7")
else:
    print("Not divisible")"""

"""a = input("Enter your name: ")
print(len(a))
print(a[0 : 1])
print(a[-1])"""

"""a = input("Enter a string: ")
if a.endswith("python"):
    print("Ends with python")
else:
    print("Does not end with python")"""

"""a = input("Enter a string: ")
if len(a) > 10:
    print("Long string")
else:
    print("Short string")"""

"""a = input("Enter a string: ")
if "@" in a or "#" in a:
    print("Special character found")
else:
    print("Clean string")"""

"""a = input("Enter a string: ")
if a[0] == a[-1]:
    print("Starting and ending character is Same")
else:
    print("Different")"""

"""a = int(input("Enter a number: "))
if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
else:
    print("False")"""

"""a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

if a > b and a > c:
    print(f"{a} is largest")
elif b > a and b > c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")"""

"""a = int(input("Enter a number: "))
if a % 7 == 0:
    print(f"{a} is multiple of 7")
else:
    print(f"{a} is not muliple of 7")"""

"""a = input("Enter a string: ")

if a.isdigit():
    print("Numbers")
elif a.isalpha():
    print("Alphabets")
else:
    print("Alpha numeric")"""

"""a = input("Enter a string: ")
if not a:
    print("String is empty")
elif a[0].isupper():
    print("First letter is capital")
else:
    print("Normal string")"""

"""a = input("Enter a string")

b = len(a)

if b % 2 == 0:
    print("Even length")
else:
    print("Odd")"""

"""a = input("Enter a string")
if a == a[ :: -1]:
    print("Palindrome")
else:
    print("Not Palindrome")"""

"""s = input("Enter a string")

if s.isdigit():
    a = "Only Numbers"
    print(a)
elif s.isalpha():
    b = "Only Alphabets"
    print(b)
else:
    c = "Special"
    print(c)

if s == s[:: -1]:
    d = "Palindrome"
    print(d)
else:
    e = "Not Palindrome"
    print(e)

f = len(s)
if f % 2 == 0:
    g = "Even Length"
    print(g)
else:
    h = "Odd Length"
    print(h)

if (len(s) >= 6 and s[0].isupper() and not s.isalpha()):
    i = "Valis Secure string"
    print(i)
else:
    j = "Week string"
    print(j)
print(f)
"""

"""a = input("Enter password: ")
length = len(a)
length_check = length >= 8
digit_check = not a.isalpha()
case_check = a.isupper()
pan_check = a != a[::-1]

if length_check and digit_check and case_check and pan_check:
    print("Strong Password")
else:
    print("Week Password")"""