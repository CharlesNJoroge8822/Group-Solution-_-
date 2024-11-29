# # QUESTION NUMBER: 1 ...

# #Write a Python program to print all numbers between two user-provided integers, skipping numbers divisible by 7.
user1=int(input("Enter your number:"))
user2=int(input("Enter Your number:"))

for num in range(user1, user2 +1 ):
    if num % 7 == 0:
        continue
    print(f"your number is :{num}")






# QUESTION NUMBER: 2 ....

#Create a Python program that calculates the maximum value among 5 numbers entered by the user. The program should:

numbers = []  # List to store the 5 numbers
for i in range(5):
    num=input(f"enter number{i+1}: ")

if num.isdigit() and int(num) != 0:
    numbers.append(int(num))

else:
    print("please enter a valid number.")
    
    #  continue
max_number = max(numbers)
print(f"Your maximum number is:{max_number} ")






# QUESTION NUMBER: 3 ....

# Write a function that takes a list of numbers and returns a new list with only the unique numbers from the original list.(list methods)
def uniqueNumbers (nums):
    unique_numbers=set(nums)
    return list(unique_numbers)
print(uniqueNumbers([1,2,2,3,4,4,5,6,]))


