'''
Write a function that returns true if the input string has the exact same number of occurrences otherwise return false.
test cases:
"aabbccdd" --> true
"abc" ---> true
"abcdd" ---> false
"hhhhheeeeeolllllo" ----> false

'''

#Optimal use dictionary to solve the problem then send to instructor

def string_occurrences(s):

    letter = {}
    for l in s:
        letter.update({l:+1})
    for l in letter:
        if l > len(letter):
            return True
        else:
          return False
    return letter
  
print(string_occurrences("aabbccdd"))