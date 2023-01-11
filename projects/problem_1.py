'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Input: "Hello World"
Output: "olleH dlroW"

Input: "A quick brown fox jumps over the lazy dog"
Output: "A kciuq nworb xof spmuj revo eht yzal god"

'''

def reverse_string(s):
    word_list = s.split()
    new_word_list = []
    for word in word_list:
        new_word_list.append(word[::-1])
    return " ".join(new_word_list)
print(reverse_string("A quick brown fox jumps over the lazy dog"))