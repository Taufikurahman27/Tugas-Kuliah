# The task of creating an integer program1
print ("================================")
print ("        Taufikurahman           ")
print ("         41823010025            ")
print ("   Task 2 Advanced programming  ")
print ("================================")


# Choosing between parts A and B
print("Select the part you want!! \n1. PART A\n2. PART B")
pilihan = int(input("Your choice of part: "))

import os

os.system('cls')

# PART A
if pilihan == 1:
    n = int(input("Enter Numbers: "))
    for i in range(n):
        print(i ** 2)

# PART B
elif pilihan == 2:
    n = int(input("Enter Numbers: "))
    for i in range(n):
        if i % 2 == 1 or i == 0:
            print(i ** 2)
else:
    print("Undefined")
