---
## Question 1
---
### Given a string `S` and two numbers `M` and `N`, write a program to print the characters of `S` that have Unicode values from `M` to `N` separated by a space

### Note

Unicode values are unique numbers that are given to every character, symbol and digit.

### Input

The first line of input contains a string representing `S`.
The second line of input contains an integer representing `M`.
The third line of input contains an integer representing `N`.

### Output

The output should be a single line containing a string that has characters that have Unicode values from `M` to `N` separated by a space.

### Explanation

For example, if the given string is `S = "words"`, and two numbers are `M = 99` and `N = 112`.

| Character | Unicode value |
| :--- | :--- |
| w | 119 |
| o | 111 |
| r | 114 |
| d | 100 |
| s | 115 |

* The characters o and d have Unicode values from 99 to 112.
* The output should be "o d".

##### Sample Input n

<\br>
```python
words
99
112
```

##### Sample Output 1

<\br>
```
o d
```
##### Sample Input 2
<\br>
```
AiRPorT
65
111
```
##### Sample Output 2
<\br>
```
A i R P o
```

---

## Question 2

---
