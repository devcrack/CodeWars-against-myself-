""" Instructions:
The goal of this exercise is to convert a string to a new string where each character in the new string 
is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.


Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 

"""

def simple_encoder(my_string):
    new_string = ""
    my_string = my_string.lower()
   
    new_string = "".join([")" if my_string.count(k) > 1 else "(" for k in my_string])

    return new_string



if __name__ == "__main__":
    # string_to_encode = "Success"
    string_to_encode = "(()))())())()("
    string_to_encode = "B(Gs(PoMhr!Tqu ZorclU" 
    string_to_encode = "aIcOzHEH)DkfqZzJHsfOfFRYgIUdNy V" # Test Result:  '()()))()()()())()())))()()()()(('

    print (string_to_encode)
    print(simple_encoder(string_to_encode))