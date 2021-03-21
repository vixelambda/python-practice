# whitespace before '('.
def z1 ():
    print ("whitespace before '('")

# missing whitespace around operator.
a=1

# missing whitespace after ','.
def z3(a):
    print(a,a)

# unexpected spaces around keyword / parameter equals.
def z4(a = 1):
    print(a)

# expected 2 blank lines, found 1.
def z5():
    return

# multiple statements on one line (colon).
if a < 1: a = 0

# multiple statements on one line (semicolon).
a = 1; b = 0

# comparison to None should be 'if cond is None:'.
if a == None:
    print("None")

# comparison to True should be 'if cond is True:' or 'if cond:'.
if a == True:
    print("True")