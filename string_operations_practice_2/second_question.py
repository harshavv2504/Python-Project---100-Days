'''

s = input()
is_alnum = True

for ch in s:
    if not (('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9')):
        is_alnum = False
        break

print(is_alnum)
# This code checks if a string contains only alphanumeric characters (letters and digits).

'''

'''

s = input()
print(all(('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9') for ch in s))


'''

'''

print(input().isalnum())
# This code checks if a string contains only alphanumeric characters (letters and digits).

'''