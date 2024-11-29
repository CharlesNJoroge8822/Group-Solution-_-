# QUESTION NUMBER : 4 ...

# Implement a function that takes a list and returns True if the list is sorted in ascending order, otherwise False.
#use of sort to either return ascending or descending order
def sorted_numbers(nums):

    if nums==sorted(nums):
     return True
 
    else:
        return False 
 
print(sorted_numbers([1,2,3,4,5,6]))

