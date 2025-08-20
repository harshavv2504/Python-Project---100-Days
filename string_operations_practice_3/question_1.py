'''
s = input()

m = int(input())
n = int(input())
line = ''
for i in s:
    if m <= ord(i) <= n:
        line += i + ' '
        
print(line.strip())

# This code takes a string input and two integers representing Unicode values.
# It then prints characters from the string that fall within the specified Unicode range, separated by spaces
'''

