from itertools import count
from math import factorial

print("                       Loops                              ")
# loops are used to repeat some work.
"""print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")"""
# manually agr lakho baar type krna ho to bht mushkil hota
# iss liay ham use kray hai loops
"""while True:
    print("Hello")"""
# iss ka yeh syntaxx hai while ke baad condition and neechay program
# ab choo ke True hai to True toT True hi hota to yeh kbi rukkay ga hi ni
# iss liay condition lgana zarooru
# phirr condition true honay pr loop khud ba khud rukk jaye ga
"""i = 1
while i <= 5:
    print("Hello")
    i += 1 """ # i = i + 1
# ab iss mai wo hi condition lga di ke i jab tak 5 se kam ya brabar hai hello print kr
# ab i ki value hona bi to zaroori thi na to ussay 1 ki value de di
# then condition lgai ke tab tak jab tak i 5 tak na jaye
# then increament ya decreament add krna hota ke kitnay tak increase ho
# to i ko 1 se increase krwa dya essay 1 2 3 4 5 ho ga
"""i = 1
while i <= 1000:
    print(f"{i} : Sorry")
    i += 1"""
# f lga kr {} ke ham variable name  bi likh sktay hai
# yeh advance method hai
"""i = 1
while i <= 5:
    print("ZAIN")
    i += 1""" # i = i + 1
"""i = 1
while i <= 100:
    print(i)
    i += 1"""
# agr coutning ko print krwana ho to simply variable ka name likh do bracket mai
"""i = 5
while i >= 1:
    print(i)
    i -= 1""" # i + i - 1
# iss trh backwaord bi print krwaya ja skta hai
# pehlay jaha se start krna wo variable ko assign krna
# then condtion kaha pr ja kr rukna
# then jo print krwana
# then yaha backwaord jana to increament ki jagga decreament
"""i = 5
while i <= 6:
    print(i)
    i -= 1""" # i = i - 1
# kbi bi essi condition ni dalni jo infinite ho
# yeh program ko kbi end hi ni honay de ga
"""i = 1
while i <= 100:
    print(i)
    i += 1""" # i = i + 1
"""n = 100
while n >= 1:
    print(n)
    n -= 1""" # n = n - 1
"""n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} multiply by {i} = {i * n}")
    i += 1"""
"""numbs = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(numbs): # i < len(numbs) - 1 yeh bi theek hai
    print(numbs[i])
    i += 1"""
# i ko index bna kr index mai likh dena
"""heroes = ["ZAIN", "EMAAN", "zain", "emaan"]
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx += 1"""
"""numbs = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 36
i = 0
while i < len(numbs):
    if numbs[i] == x:
        print(f"Founda at index: {i}")
    else:
        print(f"Not Found at index: {i}")
    i += 1"""
"""i = 1
while i <= 10:
    print(i)
    if i == 3:
        break
    i += 1
print("End of Loop")"""
# break jaha pr bi write kr do ge uss condition pr loop stop ho jaye ga
"""nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 49
i = 0
while i < len(nums):
    if nums[i] == x:
        print(f"Found at index: {i}")
        break
    else:
        print(f"Not Found at index: {i}")
    i += 1"""
# ab yaha break laga dya waha pr stop ho jaye ga
# agay found ke baad wala bi print ho rha tha
# but break lganay se yeh faida hue ke break ke baad wala print ni ho rha
"""i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1"""
# continue hota hai current task ko stop krnay ke liay
# ab jessay i 3 gya
# i 1 se increase ho gya aur continue hi gya
"""i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1"""
# ab iss cade mai jessay hi koi evan valye ayeg gi wo ussay 1 se brha kr skip kr de ga

"""lis1 = [1, 2, 3]
for el in lis1:
    print(el)"""
# loops use hotay hai cheezo ko sequently print krnay ke liay
"""nums = [1, 2, 3, 4, 5]
for val in nums:
    print(val)"""
# for lgao koi variable jis mai store krna hai then in and jiss ki stroe krna hai
# then print mai wo likh do jiss mai store kya hai na ke jiss ka store kya hai
"""veg = ["brinjal", "potato", "band ghobi"]
for el in veg:
    print(el)"""
"""tup = (1, 2, 3)
for el in tup:
    print(el)"""
# for loop ko ham kissi tuple ke upper bi lga sktay hai
# agr hamay iterator pr kaam krna to while loop
# agr data type pr krna to for
"""str1 = "Zain"
for var in str1:
    print(var)"""
# agr issay string mai kro ge to yeh individaully hr index ko print kr de ga
"""val = [1, 2, 3]
for el in val:
    if el == 2:
        print("Found")
        break
    print(el)
else:
    print("End")
print("End")"""
# ab ham for loop mai optional hai else bi use kr sktay hai
# iss ka main use  tab ata jab ham break ko use karay
# jaha ham chahtay ho break ke baad else run na karay
"""x = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in x:
    print(el)"""
"""num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 25
for el in num:
    if el == x:
        print("Found")"""


"""for el in range(4):
    print(el)
for eb in range(2, 3):
    print(eb)
for en in range(0, 10, 2):
    print(en)"""
# range
# range(start, stop, step)
# ranga ka start by dafault 0 hota hai aur step 1 hota hai
# agr ham ne range mai 1 value likhi hai to wo uss ka stop considerh ho ga
# range numbers ki sequence return krta hai data type ki ni
# jo number btaya ho uss se 1 pehlay rukk jata yeh
"""for el in range(2, 100, 2):
    print(el)"""
# to print even numbers
"""for i in range(1, 100, 2):
    print(i)"""
# to print odd numbers
"""for i in range(1, 101):
    print(i)"""
"""for i in range(100, 0, -1):
    print(i)"""
"""n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} multiply by {i} = {n * i}")"""
"""for el in range(10):
    pass
"""
# pass is used to store loop empty
# pass can also be used in if else
"""i = 5
sum = 0
for val in range(1, i+1):
    sum += val

print(sum)"""
"""n = 5
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1
print(sum)"""
# i ko baad mai update krna
"""n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print(sum)"""
"""i = 1
n = 5
fact = 1
while i <= n:
    fact *= i
    i += 1
print(fact)"""
"""n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)"""
# for mai yeh deehan rkhna jab 1 se start krna ho to 1 lazmi lgana

"""n = int(input("Enter a number: "))
i = 2
while i <= n:
    print(i)
    i += 2"""

"""n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i += 2"""

"""n = int(input("Enter a number: "))
for i in range(3, n+1, 3):
    print(i)"""

"""n = int(input("Enter a number: "))
i = 1
while i <= n:
    if i % 5 == 0:
        i += 1
        continue
    print(i)
    i += 1"""

"""n = int(input("Enter a number: "))
i = 1
while i <= n:
    if i % 5 == 0:
        i += 1
        continue
    print(i)
    i += 2"""

"""n = int(input("Enter a number: "))
for i in range(2, n+1, 2):
    if n % 3 == 0:
        i += 1
        continue
    print(i)"""

"""n = int(input("Enter a number: "))
i = 2
while i <= n:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 2"""

"""n = int(input("Enter a number: "))
i = 2
while i <= n:
    if i % 2 == 0:
        if i % 3 == 0:
            i += 1
            continue
    print(i)
    i += 1"""

"""n = int(input("Enter a number: "))

for num in range(2, n+1):
    count = 0

    for i in range(2, num):
        if num % i == 0:
            count += 1
    if count == 0:
        print(num)"""

"""n = int(input("Enter a number: "))

for num in range(2, n+1):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    if count == 0:
        print(num)"""

"""n = int(input("Enter a number: "))

for num in range(2, n+1):
    count = 0

    for i in range(2, num):
        if num % i == 0:
            count += 1

    if count == 0:
        print(f"{num} is prime")

j = 2
even_sum = 0
while j <= n:
    even_sum += j
    j += 2
print(f"Sum of all Even numbers is {even_sum}")

k = 1
odd_count = 0
while k <= n:
    odd_count += 1
    k += 2
print(f"Total numbers of Odd are: {odd_count}")

for val in range(1, n+1):
    if val % 3 == 0 or val % 5 == 0:
        continue
    print(f"{val} is not divided by 3 or 5")"""