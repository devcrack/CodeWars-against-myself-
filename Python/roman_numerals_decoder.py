"""
Instructions:
Create a function that takes a Roman numeral as its argument and returns its
value as a numeric decimal integer. You don't need to validate the form of the
Roman numeral. Modern Roman numerals are written by expressing each decimal
digit of the number to be encoded separately starting with the leftmost digit
and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC)
and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666
"MDCLXVI", uses each letter in descending order.

44 = XLIV
Example:
"""

roman_to_decimal = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

"""
My Solution
"""
def solution(roman):

    operation_value = 0
    length_string = len(roman)
    index = 0

    while index < length_string:

        if index + 1 < length_string:
            op1 = roman_to_decimal[roman[index]]
            op2 = roman_to_decimal[roman[index + 1]]
        else:
            op1 = roman_to_decimal[roman[index]]
            op2 = 0
        if op2 > op1:
            decimal_value = op2 - op1
            index += 2
        else:
            decimal_value = op1
            index += 1
        operation_value += decimal_value

    return operation_value


"""
Clever Solution
"""


def clever_solution(roman):
    dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    last, total = 0, 0
    for c in list(roman)[::-1]:
        if last == 0:
            total += dict[c]
        elif last > dict[c]:
            total -= dict[c]
        else:
            total += dict[c]
        last = dict[c]
    return total


"""
Another solution
"""


def solution2(roman): 
    romanic={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1} 
    number=0
    prev_num=0
    for i in roman:  
        number+=romanic[i] 
        if romanic[i]>prev_num: 
            number=number-(2*prev_num)
        prev_num=romanic[i]
    return number


if __name__ == "__main__":
    # roman_number = "XIX"
    roman_number = "XXI"  # 21
    roman_number = "MMVIII"  # 2008
    roman_number = "MCMXC"  # 1990
    # roman_number = "LXXIX"  # 79
    roman_number = "XLIV"
    print(solution(roman_number))

