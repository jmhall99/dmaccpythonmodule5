"""
Program: basic_for_loops.py
Author: Jeremy Hall
Last date modified: 09/26/2021

The purpose of this program is to output the content of 2 loops.
"""

#In the editor of your choice, write a Python script (.py file)
#Declare a list of floating point numbers
#Write a for loop to print each
#Write a second for loop to print the odd number descending from 99 to 33 (including 99 and 33)
#Include in .py file a docstring.

numbers = [3.14,1.21,6.66]
for num in numbers:
    print(num)

for number in range(33,101,2):
    print(number)