Avery's Notes
==============

## Commands List: 

Grep Specific:
Meant for searching specific things in a document. Kind of like a Control+F

+ X | Y :runs the output from X into Y
+ wc -l : gives the word count, make sure to run you outpu into it
+ "X" : searches for that specific item in that order
+ "^X" : makes sure that the word starts with that letter/sequence
+ "X$" : makes sure the word ends with this letter/sequence
+ "X.X" : . is like an empty spot for any letter to fill in
+ "X.*X" : makes it so any number of any different letters can fill in
+ grep -v "X" : to remove whatever the grep comman finds
+ "\+z" : one or more of the letter
+ "[abc]" : requres it to be those letters
+ "[^abc] : requires it to NOT be one of those letters
