"""
Program: input_while.py
Author: Jeremy Hall
Last date modified: 09/26/2021

The purpose of this program is to accept valid input and store in a list.
"""
#Write a small script, input_while.py that prompts the user for numeric input between 1 and 100.
#Prompt the user until the input is in the correct range. Once a the input is correct,
#store the input in a list.
#
#Script pseudocode:
#declare a list variable
#prompt and get the user input
#while user input is not good (in range)
#     prompt user for good input
#store in list
#print the list
#That's not useful! You need multiple inputs from the user,

#declare a list variable
#declare a sentinel value for user input
#prompt get the user input (indicating sentinel value to stop)
#while sentinel value is not stopping value
#while user input is not good (in range)
#            prompt user for good input
#      store in list
#      prompt and get the next user input
#
#print the list using a for loop
#Test running your script in the shell.
#Add doctring to the top of your file, add comments at the bottom with your tests and
# observed output after a few test runs of your code.
#Submit you .py file.

list = []
data = 0

while data != -99:
    data = int(input("Enter an integer between 1 and 100.  Enter -99 to quit."))
    while int(data) >= int(0) and int(data) <= int(100):
        list.append(data)
        data = -1

print(list)

#this is working as expected.  I found the pseudocode very confusing.

