# This code reads a string and prints the next character for each character in the string based on Unicode values.

'''

s = input()
next_chars = []
for char in s:
    next_chars.append(chr(ord(char) + 1))
print("\n".join(next_chars))

# This code reads a string and prints the next character for each character in the string based on Unicode values.'''


'''

def ascii_to_string(nums):
    return "".join(chr(x) for x in nums)

n = int(input())
nums = [int(input()) for _ in range(n)]
print(ascii_to_string(nums))


'''

'''

print("".join(chr(int(input())) for _ in range(int(input()))))
# This code reads a string and prints the next character for each character in the string based on Unicode values.

'''