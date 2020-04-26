# Try the Python below and answer the questions.

# Wwe assign some variables and check an expression.
# Note how we checked the expression with format
x = -1
y = 0
print("Is it true that x <= y?")
print("It's {}!".format((x<=y)))


a = 2.52
b = 5
# Notice how these two print statements give different results. Why is that?
print(a*b)
print(int(a*b)) #the first one creates a float because you're multiplying a float by int
                #the second one is an integer because you're assigning it that value

print("She said, hey there")
# Note how you can use escape sequences to format your strings as well
print("He said,\n hey there")

print("The value of a is {}.".format(a))
# Add your own

print("This is the first line, \n and this is the second line!")
