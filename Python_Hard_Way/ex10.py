#Writing some expressions with single and double-quotes
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

#List for the fat_cat
fat_cat = '%s'

#Printing all
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat % ('''
I' ll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
''')
print "I am 6'2\" tall."
print 'I am 6\'2" tall.'
