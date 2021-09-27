#Recall your input_while.py, make a copy called input_while_exit.py.
#What if the user typed bad input because they wanted to quit the entire program?
# The algorithm as written does not account for that.
#You could add code to exit the inner while if the user input a sentinel flag indicating
# they no longer have input. Implement this option by adding the appropriate exit statement
# to the inner while loop.

#Run the code.
#Notice that the code does not exit the outer while loop. There are a few ways to fix the code
# so it will exit this loop as well. Fix the code.
#Add doctring to the top of your file, add comments at the bottom with your tests and observed
# output after a few test runs of your code.
#Submit your input_while_exit.py.

list = []
data = 0

while data != -99:
    data = int(input("Enter an integer between 1 and 100.  Enter -99 to quit."))
    while int(data) >= int(0) and int(data) <= int(100):
        list.append(data)
        data = -1

print(list)