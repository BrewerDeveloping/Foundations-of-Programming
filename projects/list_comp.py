# List comprehension

# Objective's
# 1 - Faster for loops
# 2 - Simplified Conditional Statements
# 3 - String Manipulation



###############################
#         LESSON #1           #
#     Faster for Loops        #
###############################

'''
fruits = ['apples', 'bananas', 'strawberries'] #list

for fruit in fruits: #for loop
    print(fruit) #action to be done by the loop

    
[print(fruit) for fruit in fruits] #list comprehension
'''


# TAKE 1 - Without list comprehension

# fruits = ['apples', 'bananas', 'strawberries']
# new_fruits = []

# for fruit in fruits:
#     fruit = fruit.upper()
#     new_fruits.append(fruit)

# fruits = new_fruits
# print(fruits)



# TAKE 2 - With list comprehension
# .append method always takes a lot of time
# by not using .append and using a list comprehension
# we speed up the process for code to be executed

# fruits = ['apples', 'bananas', 'strawberries']
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)




###############################
#         LESSON #2           #
#    Simplified Conditional   #
#         Statements          #
###############################

# bits = [False, True, False, False, True, False, False, True]
# new_bits = []

# for b in bits:
#     if b == True:
#         new_bits.append(1)
#     else:
#         new_bits.append(0)

# super_bits = [1 if b == True else 0 for b in bits]

# print(bits)
# print(new_bits)
# print(super_bits)


###########################
#         LESSON #3       #
#    String Manipulation  #
###########################

# Customizing a messy string to make it readable with list comprehension

# my_string = "HelloMyNameIsJoshua"
# my_string = ''.join([i if i.islower() else " " + i.lower() if i in ["M", "N", "I"] else " " + i for i in my_string])[1:]
# print(my_string)