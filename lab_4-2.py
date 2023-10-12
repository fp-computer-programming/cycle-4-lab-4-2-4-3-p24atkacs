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
# lab_4-2.py
# Author: Andrew Tkacs

#write school name
school = "Fairfield Prep"

#split the schools name into two parts- starting with the first part= fairfield.
first_half = school.split(" ")[0]

#second part= prep
second_half = school.split(" ")[1]

#print it
print("First Half:", first_half)
print("Second Half:", second_half)

#combine both parts and print it.
together = first_half +  second_half
print("Full Name:", together)
