Avery's Notes
==============

### Commands List: 


## Unit 0 - General Operations

# style checker 
+ python3 ~/Code/MCB185/stylint.py <yourfile.py>
# basic commands
+ `cd /` : means to go to a different place
+ `touch` : means to create a document
+ `ls` : means to list everything in a file
+ `pwd` : tell you where you are
+ print` : writes out anything you put it
    +  `$X` : will take the input and output your individual answer ex. $USER -> avery 
+ `echo` : repeates whatever you put into it 
+ `alias XX="YY"` : changes the command

# git commands
+ `git status` : how are things? what are files doing
+ `git add` : add them to the in between
+ `git commit` : add them to my git hub
+ `git push` : 
+ `git clone` : create a duplpicate
 + `my alias`: gs=git status, gp=git add and commit, gp=git push
 
 
 
## Unit 1 - Linux

# viewing files
+ `cat` - dump the contents of files
+ `head` - print the first 10 lines of a file
+ `tail` - print the last 10 lines of a file
+ `more` - page through a file
+ `less` - page through a file with more control
+ `zless` - like `less` but works with compressed files
+ `wc` - wordcount

# directing files
+ `>` sends the stdout of a program to a file
+ `<` sends the contents of a file to the stdin of a program
+ `|` connects the stdout of one program to the stdin in of another

# creating files
+ `nano` - creates a file
+ `python3` - runs files in python
+ `rm` - remove file (delete)

# Grep Specific:
Meant for searching specific things in a document. Kind of like a Control+F

+ `X | Y` :runs the output from X into Y
+ `wc -l` : gives the word count, make sure to run you outpu into it
+ `"X"` : searches for that specific item in that order
+ `"^X"` : makes sure that the word starts with that letter/sequence
+ `"X$"` : makes sure the word ends with this letter/sequence
+ `"X.X"` : . is like an empty spot for any letter to fill in
+ `"X.*X"` : makes it so any number of any different letters can fill in
+ `grep -v "X"` : to remove whatever the grep comman finds
+ `"\+z"` : one or more of the letter
+ `"[abc]" `: requres it to be those letters
+ `"[^abc]"` : requires it to NOT be one of those letters


## Unit 2 - Calculations

# math operations


| Operator | Purpose           | Example             | Output
|:---------|:------------------|:--------------------|:------
| `+`      | addition          | `print(1 + 1)`      | 2
| `-`      | subtraction       | `print(1 - 1)`      | 0
| `*`      | multiplication    | `print(2 * 2)`      | 4
| `/`      | division          | `print(1 / 2)`      | 0.5
| `**`     | exponentiation    | `print(2 ** 3)`     | 8
| `//`     | integer divide    | `print(5 // 2)`     | 2
| `%`      | remainder         | `print(5 % 2)`      | 1
| `()`     | precedence        | `print(5 * (2 + 1))`| 15

# math functions

| Function              | Purpose
|:----------------------|:---------------------------
| `abs(x)`              | absolute value of `x`
| `pow(x, y)`           | `x` to the power of `y`
| `round(x, ndigits=3)` | round off `x` to 3 digits
| `math.ceil(x)`        | round `x` up
| `math.floor(x)`       | round `x` down
| `math.log(x)`         | `x` in log base e
| `math.log2(x)`        | `x` in log base 2
| `math.log10(x)`       | `x` in log base 10
| `math.sqrt(x)`        | square root of `x`
| `math.pow(x, y)`      | `x` to the power of `y`
| `math.factorial(n)`   | factorial of integer n

# math constants
+ `math.e`:  2.71828...
+ `math.pi`: 3.14159...
+ `math.inf`: infinity
+ `math.nan`: not a number (e.g. 0/0)

# writing a function
```
def functionname(a, b):   #how you format the input of the variables
    return math.sqrt(a**2 + b**2) 
```
# operating a function & conditionals
`print(functionname(3, 4)) #make sure it is the same format of earlier`

# numerical comparison operators

| Operator | Purpose           | Example
|:---------|:------------------|:----------------------
| `==`     | equality          | `if a == b:`
| `!=`     | inequality        | `if a != b:`
| `<`      | less than         | `if a < b:`
| `>`      | greater than      | `if a > b:`
| `<=`     | less or equal     | `if a <= b:`
| `>=`     | greater or equal  | `if a >= b:`

