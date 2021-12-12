"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

# most clever solution
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

# Second best solution
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
    

# my solution    
def str_to_camel_case(text):
    _str = ""
    to_upper = False
    for i in range(0, len(text)):        
        if (text[i] == '_' or text[i] == '-'):
            to_upper = True
            continue
        if to_upper:
            _str += text[i].upper()
            to_upper = False
        else:
            _str += text[i]
    return _str

if __name__ == "__main__":
    # random_string = "the-stealth-warrior"
    random_string = "a_Cat-is_kawaii"
    #random_string = "the_Cat-was-Pippi" # 
    random_string = "The_cat-Is-pippi" # => TheCatIsPippi
    print(f"Input => {random_string}")
    print(str_to_camel_case(random_string))


# 'aCatIsKawaii