

def ini_array(_str1, _str2):
    m = len(_str1)
    n = len(_str2)
    array =[[0] * (m + 1) for _ in range(n + 1)]
    for j in range(1, m + 1):
        array[0][j] = _str1[j -1] 
    for i in range(1, n + 1):
        array[i][0] = _str2[i -1]
    
    return array

def pretty_print(an_array):
    for i in range(len(an_array)):
        str_to_print = ""
        for j in range(len(an_array[0])):           
            str_to_print += str(an_array[i][j]) + " "
        print(str_to_print + "\n")

if __name__ == "__main__":
    #str1 = str(input("String 1 please:"))
    #str2 = str(input("String 2 please:"))

    str1 = "BDCAB"
    str2 = "ABCBDAB"
    print(str1)
    print(str2)

    arr = ini_array(str1, str2)
    
    print()
    print()
    print(arr)
    print()
    print()
    pretty_print(arr)

            
