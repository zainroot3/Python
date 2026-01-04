#               Loops
"""
loops allow us to execute the block of code multiple times
which is specially used for repetitive tasks
"""
#for loop
#while loop
#break and continue
#nested

# All about for loop
"""
runs a block of code for each item in sequence,
like a list or range
"""
# to print tha whole list
fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    print(fruits)
# to print range
"""
for f in range(start, stop, step)
    print(f)
"""
#for f in range(1, 10): # it will not add 10 it adds all numbers before 10
# print(f)
# to do print all we need to add step
for q in range(1, 11, 2): # it will add data now in +2
    print(q)

print("while loop")
"""
runs as long as the
condition becomes true
"""
count = 0
while count < 5:
    print(count)
    count += 1 # used to tell how much number will be added

print("Break and Continue")

for number in range(1, 11):
    if number == 5:
        break # it will exit the loop when number reach at 5
    elif number % 2 == 0:
        continue # it will skip even number
    print(number)
# it will print all even numbers until 5

print("Nested Loop")

for i in range(3):
    for k in range(2):
        print(i, k)