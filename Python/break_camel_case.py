
# Best rate solution 
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

# Second best rate solution
import re
def solution(s):
    return re.sub('([A-Z])', r' \1', s)
    
# My Solution
def sol2(s):
    s2 = ""

    for i in range(0, len(s)):        
        if s[i].isupper():
            s2 += " "
        s2 += s[i]
    return s2



if __name__ == "__main__":
    _s = "helloWorld"
    _s = "breakCamelCase"
    _s = "CaseBreakCamelCase"
    #_s = "helloWorld"
    print(sol2(_s))
