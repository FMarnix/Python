#Importing the arguments
from sys import argv

#What are the arguments
script, filename = argv

#Type of file executions
txt = open(filename)

#Printing an informative statement
print "Here's your file %r:" % filename

#Calling the function in txt type
print txt.read()

#Another loop to print the same file again
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
