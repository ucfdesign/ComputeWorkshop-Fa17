"""

boolean-0.py

Josh Kaplan
jk@ucf.edu

Some examples of boolean expressions

"""

# Python has values "True" and "False". Note they MUST be capitalized.
print("True == True evaluates to", True == True)
print("True == False evaluates to", True == False)
print("True != False evaluates to", True != False)
print("True is True evaluates to", True is True)
print("True is not False evaluates to", True is not False)

# Here some numerical examples.
print("1 < 2 evaluates to", 1 < 2)
print("2 > 3 evaluates to", 2 > 3)
print("0 < 1 < 3 evaluates to", 0 < 1 < 3)
print("1 == True evaluates to", 1 == True)

# Let's define a variable. We'll call it x.
x = 10
print("x > 0 and x < 10 evaluates to", x > 0 and x < 10)

# We can also use the "and" and "or" operators to combine conditions
print("x < 1 or x == 10 evalutes to", x < 1 or x == 10)
print("0 < x < 20 evaluates to", 0 < x < 20)
