
# Without using any built-in functions, write a program to find the first word in a string `S` that comes first in dictionary order.

'''
s = input()

first = ""     # store the first word
word = ""      # build current word

for i in range(len(s)):
    char = s[i]
    if char != " ":
        word += char   # keep building
    if char == " " or i == len(s) - 1:  # word boundary
        if first == "" or word.lower() < first.lower():
            first = word
        word = ""   # reset for next word

print(first)
'''

 


# with using sorted function
'''
S = input().split()

# sort words ignoring case
S.sort(key=str.lower)

# print the first word
print(S[0])
'''


# with using min function

'''

S = input().split()
# find the minimum word ignoring case
first_word = min(S, key=str.lower)
print(first_word)

'''