"""
Description

Description:
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""

# Most Clever solution:
def countBits(n):
    return bin(n).count("1")

# second rated solution 

def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total

# Third solution

def countBits(n):
    return bin(n)[2:].count('1')


# Other curious solution

def countBits(n):
    ret = 0
    while n:
        ret += n & 1
        n >>= 1
    return ret

# My solution 

def count_bits(n):
    return list(format(n, "b")).count("1")