"""
Instructions:
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), 
from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
"""
# My solution
def divisors(n):
    values = []
    for i in range (2, n):
        if n % i == 0:
            values.append(i)
    return values if values else f"{n} is prime"
    return values

if __name__ == "__main__":
    print(divisors(7))


# Clever solution 
def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l


# Second rated solution 
def divisors(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n
    

# Test cases
import codewars_test as test
from solution import divisors

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(divisors(15), [3,5])
        test.assert_equals(divisors(253), [11,23])
        test.assert_equals(divisors(24), [2,3,4,6,8,12])
        test.assert_equals(divisors(25), [5])
        test.assert_equals(divisors(13), "13 is prime")
        test.assert_equals(divisors(3), "3 is prime")
        test.assert_equals(divisors(29), "29 is prime")
