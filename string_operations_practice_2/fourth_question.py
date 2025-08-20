# This code finds the first and last words in a string based on dictionary order.
# It does not use any built-in functions for string manipulation.

'''s = input()

first = None
last = None
word = ""

for i in range(len(s)):
    char = s[i]
    if char != " ":
        word += char
    
    if char == " " or i == len(s)-1:  # end of word
        if first is None or word.lower() < first.lower():
            first = word
        if last is None or word.lower() > last.lower():
            last = word
        word = ""  # reset for next word

print(first, last)
'''


## This code finds the first and last words in a string based on dictionary order using sorting.
# It sorts the words and then retrieves the first and last words from the sorted list.

'''
S = input().split()

# sort words ignoring case
S.sort(key=str.lower)

# first word = S[0], last word = S[-1]
print(S[0], S[-1])
'''
