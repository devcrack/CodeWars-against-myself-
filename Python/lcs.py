
def ini_array(_str1, _str2):
    m = len(_str1)
    n = len(_str2)
    array =[[0] * (m + 1) for _ in range(n + 1)]
    for j in range(1, m + 1):
        array[0][j] = _str1[j - 1]
    for i in range(1, n + 1):
        array[i][0] = _str2[i - 1]

    return array


def pretty_print(an_array):
    for i in range(len(an_array)):
        str_to_print = ""
        for j in range(len(an_array[0])):
            str_to_print += str(an_array[i][j]) + " "
        print(str_to_print + "\n")


def calc_lcs_array(an_array):
    i_i, j_j = 1, 1

    for i in range(1, len(an_array)):
        i_i += 1
        for j in range(1, len(an_array[0])):
            j_j += 1
            i_val = an_array[i][0]
            j_val = an_array[0][j]
            print(f"Comparing: {i_val}, {j_val}")

            if an_array[i][0] == an_array[0][j]:
                print(f"{an_array[i][0]} is Equal to: {an_array[0][j]}")
                an_array[i][j_j] = an_array[i][j] + 1
                # an_array[i_i][j_j] = an_array[i_i - 1][j_j - 1] + 1
            else:
                print("Not equal")
                an_array[i_i][j_j] = max(an_array[i][j_j], an_array[i_i][j])


def ini_array_aproach2(_str1, _str2):
    _i = list(_str2)
    _i.insert(0, 0)
    _j = list(_str1)
    _j.insert(0, 0)
    an_array = [[0] * len(_j) for _ in range(len(_i))]

    return _i, _j, an_array


def calc_lcs_approach2(array_i, array_j, array_to_calc):
    ii = 1
    for i in array_i:
        jj = 1
        for j in array_j:
            if i == j:
                array_to_calc[ii][jj] = array_to_calc[ii - 1][jj - 1] + 1
            else:
                array_to_calc[ii][jj] = max(array_to_calc[ii - 1][jj], array_to_calc[ii][jj - 1])
            if jj + 1 < len(array_j):
                jj += 1
            else:
                break
        if ii + 1 < len(array_i):
            ii += 1
        else:
            break


def calc_lcs_approach2(array_i, array_j, array_to_calc):
    ii = 1
    for i in range(1, len(array_i)):
        jj = 1
        for j in range(1, len(array_j)):
            if array_j[j] == array_i[i]:
                array_to_calc[ii][jj] = array_to_calc[ii - 1][jj - 1] + 1
            else:
                array_to_calc[ii][jj] = max(array_to_calc[ii - 1][jj], array_to_calc[ii][jj - 1])
            if jj + 1 < len(array_j):
                jj += 1
            else:
                break
        if ii + 1 < len(array_i):
            ii += 1
        else:
            break

    for i in range(len(array_i), 0, -1):
        to_print = ""
        for j in range(len(array_j), 0, -1):
            to_print += str(array_to_calc[i - 1][j - 1]) + " "
        print(to_print)




def pretty_print_approach2(columns, rows, lcs_array):
    for i in range(1, len(rows) + 1):
        i = i - 1
        to_print = ""
        for j in range(1, len(columns) + 1):
            j = j - 1
            to_print += str(lcs_array[i][j]) + " "
        print(to_print)


if __name__ == "__main__":
    # str1 = str(input("String 1 please:"))
    # str2 = str(input("String 2 please:"))
    str2 = "ABCBDAB"
    str1 = "BDCAB"

    # str1 = "AGGTAB"
    # str2 = "GXTXAYB"

    # print(str1)
    # print(str2)
    #
    # arr = ini_array(str1, str2)
    #
    # print()
    # print()
    # print(arr)
    # print()
    # print()
    # pretty_print(arr)
    # calc_lcs_array(arr)
    # pretty_print(arr)
    i, j, _array = ini_array_aproach2(str1, str2)
    print(i)
    print(j)
    # pretty_print(_array)
    # pretty_print_approach2(j, i, _array)
    calc_lcs_approach2(i, j, _array)
    print("JEJE")
    # pretty_print(_array)
