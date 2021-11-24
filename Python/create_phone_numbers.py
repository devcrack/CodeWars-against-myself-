# Best reate solution
"""
Instructions
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
"""
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# Second

def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])

# Mystics solution
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number(n):
    return "(%i%i%i) %i%i%i-%i%i%i%i" % tuple(n)


# I consider this the best solution
def create_phone_number(n):
    n = "".join([str(x) for x in n] )
    return("(" + str(n[0:3]) + ")" + " " + str(n[3:6]) + "-" + str(n[6:]))



# My solution
def create_phone_number(n):
    number_phone = "("
    for index, value in enumerate(n):
        if index == 3:
            number_phone += ") "
        elif index ==6:
            number_phone += "-"
        number_phone +=str(value)
    return number_phone
            