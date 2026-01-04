# print("Functions               and               Recursion")
"""a = 90
b = 89

sum = a + b
print(sum)

# more lines of code

a = 89
b = 5478

sum = a + b
print(sum)"""
# ab yaha pr ham baar baar sum kr rhay
# beech mai more lines of code bi a rhi
# but yeh zyada code ke liay baar baar alag alag jagga pr code likhna mushkil ho jata hai
# to uss ke liay ham function mai code likh letay hai
# aur need prnay pr simply function ko call kr letay hai
# functions ka main use keh saktay hai repeated cheezo ko kam krna
"""def name():
    print("Zain")

name()
name()
name()"""
# def use hota function bnanay ke liay
# baad mai funtion ka name likhna hai and () and :
# then function ka kaam uss ke neechay likh dena hai
# then jaha pr function ko use krna hai simple ussay call kr dena hai
"""def Calc_sum(a, b):
    total = a + b
    print(total)

Calc_sum(10, 8)"""
# ham function ke andr perimeteres ko bi add kr sktay hai jessay a and b
# then uss ke andr  kaam perfrom pr ke print kr sktay hai
# return bi kr sktay hai value ko
# then jaha pr use krna simply function call and perimeters ki value
"""def a_sum(a, b):
    print(a + b)
    return a + b

a = a_sum(10, 11)
print(a)"""
# agr return use ni karay ge to print none return karay ga
"""def calc(a, b):
    return  a + b

total = calc(10, 23)
print(f"The sum is {total}")"""
# iss trh se simple return se bi kaam chal jaye ga
# mgr choo ke wo value return kr rha
# to ussay kissi variabe  mai store kr ke phirr print krwana paray gaa
"""def average(a, b, c):
    avg = (a + b + c) / 3
    print(avg)
    return avg

a = average(10, 20, 30)
print(a)"""
# iss trh ke case mai print bi kr sktay hai aur return bi kr sktay hai apni mrzi hai
# hn but return ke liay issay print krna prta yeh yaad rkhna
"""print("Zain", end = " ")
print("Naveed")"""
# print built in function hai
# iss mai specify krnay ki zaroorat ni comma khud space daal deta
# and new print automatically new line daal deta
# agr end ko change krna ho to wo kya ja skta simplye write end  and iss ki value pass kr do
"""def sum(a, b = 2):
    sum = a + b
    print(sum)

sum(1, 3)"""
# agr ham chahtay hai ke perimtors mai koi value na ho to
# ham koi dafault value bi set kr sktay hai
# aur hn pehlay end walay ko value deni phirr pehlay
# aur agr ham ne assign bi ki aur khud bi daal rhay
# to wo wali consider ho gi jo ham ne khud daali ho
"""cities = ["Sialkot", "Lahore", "Karachi"]
names = ["Zain", "Emaan", "Zain", "Emaan"]

def length(a):
    print(len(a))

length(cities)
length(names)
"""
"""cities = ["Sialkot", "Lahore", "Gujrat", "Karachi", "Gujranwala"]

def arr(a):
    print(cities[0], cities[1])

arr(cities)"""
"""cities = ["Sialkot", "Karachi", "Lahore", "Gujranwala", "Gujrat"]

def length(a):
    for list in a:
        print(list, end = " ")

length(cities)"""

"""n = int(input("Enter a number: "))

def fact(n):
    count = 1
    for i in range(1, n+1):
        count *= i
    print(count)

fact(n)"""
"""def converter(usd):
    pkr = usd * 280.16
    print(f"{usd} USD = {pkr} PKR")

n = float(input("Enter numbers of USD you want to convert in PKR: "))
converter(n)"""
"""def even_odd():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")

def sum1():
    a = float(input("Enter 1st number: "))
    b = float(input("Enter 2nd number: "))
    total = a + b
    print(f"Sum of {a} and {b} is = {total}")

z = int((input("What you want to find: \n 1: Sum of 2 numbers \n 2: Check number is Even or Odd \n Enter option: ")))
if z == 1:
    sum1()
elif z == 2:
    even_odd()
else:
    print("You entered wrong option")"""

"""print("Student     Utility     System")
print("1: Add Student ")
print("2: Password Strength Checker: ")
print("3: Number Analyser ")

def per(a, b):
    percentage = (a / b) * 100
    return percentage

def grade(a, b):
    if (a >= 90) and (a <= 100):
        print(f"{b} got A grade")
    elif (a >= 80) and (a < 90):
        print(f"{b} got B grade")
    elif (a >= 70) and (a < 80):
        print(f"{b} got C grade")
    elif a < 70:
        print(f"{b} You are Fail")
    else:
        print("Kindly check your percentage is it in numbers")

def wrong():
    print("You entered wrong option")

def pass_palindrome(a):
    if (a == a[ :: -1]):
        print("Password is Palindrome")
    else:
        print("Password is not Palindrome")

def pass_length(a):
    if len(a) >= 8:
        print("Your password is Strong")
    else:
        print("Your password is Weak")

def even_odd(a):
    if a % 2 == 0:
        print(f"{a} is Even")
    else:
        print(f"{a} id Odd")

def calc(a, b, c):
    if c == "+":
        sum1 = a + b
        print(f"Sum of {a} and {b} is {sum1}")
    elif c == "-":
        sub1 = a - b
        print(f"Subtraction of {b} from {a} is {sub1}")
    elif c == "*":
        mul1 = a * b
        print(f"Multiplication of {a} and {b} id {mul1}")
    elif c == "/":
        div1 = a / b
        print(f"Division of {a} and {b} is {div1}")
    else:
        print("Enter a correct option")

number = int(input("Enter your choice: "))
if number == 1:
    a = input("Enter Student name: ")
    print("1: Find Percentage ")
    print("2: Find Grade ")
    b = int(input("Enter your option: "))
    if b == 1:
        t = float(input("Enter total marks: "))
        o = float(input("Enter obtained marks: "))
        ob = per(o, t)
        print(f"{a} you obtained {ob} %")
    elif b == 2:
        g = float(input("Enter your percentage: "))
        grade(g, a)
    else:
        wrong()
elif number == 2:
    print("1: Check password is palindrome or not")
    print("2: Check Length of password is strong or not")
    p = int(input("Enter your option: "))
    if p == 1:
        password = input("Enter your password: ")
        pass_palindrome(password)
    elif p == 2:
        password = input("Enter your password: ")
        pass_length(password)
    else:
        wrong()
elif number == 3:
    print("1: Even/Odd Calculator")
    print("2: Calculator")
    c = int(input("Enter your option: "))
    if c == 1:
        ca = int(input("Enter a number: "))
        even_odd(ca)
    elif c == 2:
        ca = float(input("Enter 1st number: "))
        cb = float(input("Enter 2nd number: "))
        cc = input("What operation you want to perform: (+, -, *, /)")
        calc(ca, cb, cc)
    else:
        wrong()
else:
    wrong()"""

# ab recursion zaroori ni hacking mai but understanding ho to acha hai

"""def show(a):
    if a == 0:
        return 
    print(a)
    show(a - 1)

a = int(input("Enter a number: "))
show(a)"""
# ab iss mai print krna hota
# then function ko call kr ke operation btana hota
# then upper condition lgani hoti ke stop kaha pr krna hai
# jo kaam recursion se ho sktay wo saray kaam loops se bi ho sktay hai
# aur jo kaam loops se ho sktay hai wo saray kaam recusrion se bi ho sktay hai

"""def factoral(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factoral(n - 1)

n = int(input("Enter a number you want to find factorial: "))
a = factoral(n)
print(a)"""
# ab yeh yaad rkhnajab bi recursion use karay ge wo chlti jaye gi jab tak stoping condition true na ho as same as loops
# iss mai n ko uss se minus se mulitply kr rha
# aur tab tak krta jaye ga jab tak wo 0 ya 1 ke equal na a jaye

"""print("Student \t Management \t System")

def menu():
    print("1: Add Student")
    print("2: Remove Student")
    print("3: View Student Details")

def add(details):
    Add_a = input("Enter Student Name: ")
    Add_b = int(input("Enter Student Class: "))
    Add_c = int(input("Enter Roll No: "))
    Add_d = int(input("Enter Student Age: "))
    Add_e = int(input("Enter Student Phone Number: "))
    Add_f = input("Enter Student Valid Address")
    Add_g = input("Enter Student Father Name: ")
    Add_h = int(input("Enter Student Father Phone Number: "))
    details.update({"Name" : Add_a})
    details.update({"Class" : Add_b})
    details.update({"Roll No" : Add_c})
    details.update({"Age" : Add_d})
    details.update({"Phone: " : Add_e})
    details.update({"Address: " : Add_f})
    details.update({"Father Name" : Add_g})
    details.update({"Father Phone" : Add_h})

def remove(details):
    details.clear()

def wrong():
    print("Please Enter a valid option")

menu()
value = int(input("Choose your option: "))

details = {}
if value == 1:
    add(details)
    print(" \n Student Details Added Successfully")
elif value == 2:
    remove(details)
    print("Student Details Removes Successfully")
elif value == 3:
    print(details)
else:
    wrong()"""

"""def print_list(list, idx = 0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx + 1)

a_fruits = ["Apple", "Banana", "Lichi"]
print_list(a_fruits)"""