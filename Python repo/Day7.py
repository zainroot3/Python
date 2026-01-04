# f = open("File Name", "Mode")
# kissi bi file ko read ya write krney ke liay pehlay ussay open krna hota
# then simply open fucntion se ham file ko open kr sktay hai
# () mai pehlay to file ka name likhna hai then mode mtlb kya kaam krna hai
# 2 hi mode zyada use krnay  hai 1 read and 1 write
# inn ko use krnay ke liay ham r and w use krtay hai
# dafault paramter iss ka read hota hai agr koi bi pass na ho to
# agr file same folder mai na ho to complete path type krna hota hai
"""f = open("Zain.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()"""
# kissi bi file ko pehlay open krna hota hai
# then uss ke andr kya krna hai wo btana hota hai
# iss mai ham ne file ko open kya
# ussay read ki permissions de di
# ussay f ke equal kr dya
# then f ko read kr lya simple .read function se yeh saari file read karay ga
# then ussay variable ko assign kr ke print krnay ke liay data ke equal kr dya
# aur screen pr print krnay ke liay data ko print ke andr
# you can also print type of data
# ab achay programmer ki nishani hai ke file open kr ke kaam kr ke file close kr de
# takkay kissi aur command se file pr koi impact na ho
# iss ke liay simply file ko f se aur .close function use ho ga

# SOME OPTIONS AND THEIR DESCRICTION THAT WE CAN USE IN MOD

#   CHARACTER                                 MEANING
"""
        r                      open for reading (dafault)
        w                      open for writing and truncating file
        x                      create a new file and open it for writing
        a                      open for writng, apppending to the end of file if exist
        b                      binary mode
        t                      text mode (dafault)
        +                      open a disk file for updating (reading and writing)
  """
# w mai truncating mean overwrite mean pehlay poora file empty ande new write sab kuch
# w hota delete kr ke write ussi trh
# a hota jitna likha uss ke agay se likhna
# 2 mods ko combine bi kya ja skta
# ab dafault t hota to upper walay mai ham ne t ni likha kyu ke file t wali thi
# but agr binary file hoti to hamay b add krna prta
# agr 2 operations ko 1 saath use krna ho tab ham + use krtay hai
# mean w meann write to + add karay ge to read and write w+ ho jaye ga
# a mean append to a+  mean write bi
"""f = open("Zain.txt", "r")

data = f.read(5)
print(data)

f.close()"""
# agr ham bracket ke andr paremater use karay to yeh utnay character print karay ga phirr tab
"""f = open("Zain.txt", "r")

data = f.readline()
print(data)

data1 = f.readline()
print(data1)

data2 = f.readline()
print(data2)

f.close()"""
# agr read ko readline kr de ge to yeh sirf 1 line print karay ga
# aur 2nd wali print krni to pehly 1 phirr 2 then 3 issi trh print krna ho ga
"""f = open("Zain.txt", "r")

data = f.read()
print(data)

data1 = f.readline()
print(data1)

f.close()"""
# important point agr 1 dfa ham ne kissi file ko complete read kr dya hai to baad mai agr ham
# uss ki line print krtay hai to wo ni ho gi
# sirf 1 hi baar poori file read ho gi
# kyu kw 1 function ke baad next function waha se chlta hai jaha function end hua ho
# to read ne to poori file read kr di
# neechay to bss space bachi to space print ho gi
"""f = open("Zain.txt", "w")

f.write("I am Zain")

f.close()"""
# w tab use krna jab ham ne poorani file delete kr ke new add krna ho ussi ke andr
# yeh write mean hai but kaam overwrite hai iss ka
"""f = open("Zain.txt", "a")

f.write("\nI am Learning Hacking")

f.close()"""
# agr jo file hai ussi ke andr uss ke end se likhna hai to ham a use karay ge
# write krnay ke liay wo hi .write function use ho ga
# ham ne bss sahi mod lgana ke ham kaam kya krna chahtay hai
# aur yeh pehli line ke agay likhta hai new line pr ni
# new line pr likhnay ke liay alag se \n likhna prta hai
"""f = open("Zain1.txt", "w")
f.close()"""
"""f = open("Zain1.txt", "a")
f.close()"""
# agr aap write ya append krtay hai aur file exist ni krti
# to python khud ba khud uss name se file bna de ga
# a+ mai jo ham likhtay cheezay start mai overwrite ho jatu
# end mai jo bach jata wo wessay ka wessa rehta
"""with open("Zain.txt", "r") as f:
    data = f.read()
    print(data)"""
# 1 yeh bi tareeka hota hai file ko open karnay ka
# with se start kr ke open karo and end mai as f
# then ham same f pr operations perform kr sktay hai
# with ka yeh faida hai ke yeh automatically file ko close kr de ga
# iss mai close function compulsary ni hai
# kyu ke aap dekh sktay yeh if else ki trh 4 spaced chorr kr ho rha
# to data bss wo hi ho ga jo 4 spaces wala
# jab spaces ko end kya wo khud ba khud issay close kr de ga
"""with open("Zain.txt", "w") as f:
    f.write("My name is Zain")"""
# issi trh read write and all operations kiyen ja sktay hai with se bhi
"""import os
os.remove("Zain.txt")"""
# agr kissi bi file ko delete krna ho to uss ke liay hamay os module ko import krna prta
# then os .funtion to remove krnay ke liay remove funtion
# then location aur agr file same folder mai hai to file name
"""with open("practice.txt", "w") as f:
    f.write("Hi Everyone")
    f.write("\nI am learning file I/O")
    f.write("\nUsing Java")
    f.write("\nI like programming in Java")"""
# iss trh se aap koi bi file bna kr uss mai data write kr sktay hia
# ab new file bnani thi to file ko write kr ke name de do file khud ba khud ban jaye gi
"""with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)"""
# ab file mai data ko replace krna tha
# pehlay to file ko read kr lo aur variable mai store kr lo
# then new variable bna kr replace command se data replacae kr do
# then simply just data overwrite kr do
"""word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if data.find("learning") != -1:
        print("Found")
    else:
        print("Not Found")"""
# agr koi word find krna ho to file ko read pr open kro
# then ussay variable ke equal kro
# then ,find function se check hota available hai ya ni
# aur != -1 ata hai

                         # AI USE KRO BAAKI KYA ZAROORAT ITNAY DEEP KI