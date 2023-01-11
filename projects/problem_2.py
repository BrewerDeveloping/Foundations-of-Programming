'''
// Filter Largest Challenge

// TODO: Write a function that takes in an array containing numerical values, and returns a new array with the largest value removed.

// NOTE: There might be duplicate values. Values might be positive or negative. 
The original array should not be modified, and the items should remain in the same order as before for the returned array.

// NOTE: For this challenge, we will ask you to NOT use any array functions (including map()/filter()/sort()) nor use Math.max() 

// Test Case: [7,2,5,7,1] ...returns [2,5,1]
'''

def largest_value_removed(nums):
    # Define Variable's
    larg_val = 0
    #nums = [7,2,5,7,1] # Don't Change original list
    removed_nums = []
    nums2 = nums # Changed list
    #retrieving the larg_val
    for number in nums2:
        if number > larg_val:
            larg_val = number
    for number in range(len(nums2)):
        if nums2[number] == larg_val:
            removed_nums.append(number)
            larg_val2 = removed_nums
    for number in sorted(larg_val2, reverse = True):
        if number < len(nums2):
            nums.pop(number)
    return nums2

print(largest_value_removed([7,2,5,7,1]))