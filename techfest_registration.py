# TechFest Registration System A Python program that records event participants and analyzes track diversity.


# Task 1: Registration Setup
print("Welcome to SMIT TechFest!")
print("Event organized by Philip Andrei Teves of APPDAET BTCS2\n")

# Ask user how many participants will join
num_participants = int(input("How many participants will register? "))

if num_participants <= 0:
    print("Invalid number of participants.")
else:
