# %d is a formatter 
x = "There are %d types of people." % 10

# Set the variable binary to a string 
binary = "binary"

# Set the variable do_not to the string of don't
do_not = "don't"

# Subsitute variables in a string. When using multiple, enclose them with a parenthesis and comments between.
y = "Those who know %s and those who %s." % (binary, do_not)

# Sent output of x variable to std out
print x 

# Send output of y variable to std out
print y

# Send output of x variable with formatting of %r - raw data of the variable
print "I said: %r." % x

# Send output of y variable with formatting o %s - no ticks so have to add them.
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

