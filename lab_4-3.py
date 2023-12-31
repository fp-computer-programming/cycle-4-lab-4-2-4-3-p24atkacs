"""
Create a Python file named lab_4-2.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a Python file named lab_4-2.py
Create a variable called school and set it equal to "Fairfield Prep".
Write a statement that splits "Fairfield" and stores it as first_half, and a similar statement that splits " Prep" and stores it as second_half.
Print each half on its own line, then print the two halves joined together using concatenation.

____________________________________

Create a Python file named lab_4-3.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Write a program that contains a conditional similar to that on slide 4 that will compare two strings 
provided by the user and return if the strings are equal, one string is greater than the other, or one string is less than the other.


"""
# lab_4-3.py
# Author: Andrew Tkacs

# Get two strings from the user.
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Compare the two strings in terms of if they are equal or one is greater or less than the other and provide the result.
if string1 == string2:
    print("The strings are equal.")
elif string1 < string2:
    print("The first string is less than the second string.")
else:
    print("The first string is greater than the second string.")
