---
## Question 1:
---

### Given a string `S`, write a program to print the next characters of all characters in `S` based on the Unicode value, each on a new line

### **Input**

The input will be a single line containing a string representing `S`.

### **Output**

The output should contain the next characters of all characters in `S` based on the Unicode value, each on a new line.

### **Explanation**

For example, if the given string is `S = "coding"`,

* The characters in the given string are **c**, **o**, **d**, **i**, **n**, and **g**.
* The next characters of characters in `S` are:

| Character - Unicode | Next character - Unicode |
| :--- | :--- |
| c - 99 | d - 100 |
| o - 111 | p - 112 |
| d - 100 | e - 101 |
| i - 105 | f - 102 |
| n - 110 | g - 103 |
| g - 103 | h - 104 |

---

## Question 2

---

### Given a variable name `S`, check if `S` is a valid variable name. The variable name is valid if it contains only upper case letters, lower case letters, and digits

### Print True if `S` is a valid variable name. Otherwise, print False

### Note

* The Unicode values of upper case letters ( `A` - `Z` ) are from 65 to 90.
* The Unicode values of lower case letters ( `a` - `z` ) are from 97 to 122.
* The Unicode values of digits ( `0` - `9` ) are from 48 to 57.

### Input

The input will be a single line containing a string representing `S`.

### Output

The output should be a single line containing a boolean. `True` should be printed if `S` is a valid variable name. Otherwise, print `False`.

---

## Question 3

---

### Given a sentence `S` contains space-separated words, write a program to print the word that comes first when the words are in dictionary order

### Note

* Consider both uppercase and lowercase alphabets as the same.
* Dictionary order is a way of ordering words or sequences of characters based on their alphabetical order.

### Input

The input will be a single line containing a string representing `S`.

### Output

The output should be a single line containing a string that is a word in the given sentence that comes first when the words are in dictionary order.

### Explanation

For example, if the given sentence is `S = "He is bit slow"`,

* The words in the given sentence are He, is, bit, and slow.
* The words in the given sentence in dictionary order are bit, He, is and slow.
* The word in the given sentence that comes first in the dictionary is bit.

---
Question 4

---

### Given a sentence `S` contains space-separated words, write a program to print the first and the last words of the sentence in dictionary order separated by a space

### Note

* Consider both uppercase and lowercase alphabets as the same.
* Dictionary order is a way of ordering words or sequences of characters based on their alphabetical order.

### Input

The input will be a single line containing a string representing `S`.

### Output

The output should be a single line containing a string obtained by joining the first and last words of the sentence in dictionary order with a space.

### Explanation

For example, if the given sentence is `S = "to get the Ball rolling"`,

* The words in the sentence are to, get, the, Ball, and rolling.
* The words in dictionary order are Ball, get, rolling, the, and to.
* The first word is Ball.
* The last word is to.

The output should be Ball to.
