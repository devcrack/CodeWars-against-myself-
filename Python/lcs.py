
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

    index_i = len(array_i) - 1
    index_j = len(array_j) - 1
    _lcs = ""

    while True:
        if index_i == 0 or index_j == 0:
            break
        val_i = array_i[index_i]
        val_j = array_j[index_j]

        if val_i == val_j:
            _lcs = val_i + _lcs
            # _lcs.insert(0, val_i)
            index_j -= 1
            index_i -= 1
        else:
            left_diagonal = array_to_calc[index_i][index_j - 1]
            right_diagonal = array_to_calc[index_i - 1][index_j]

            if left_diagonal > right_diagonal:
                index_j -= 1
            else:
                index_i -= 1

    return _lcs
    # for i in range(len(array_i), 0, -1):
    #     to_print = ""
    #     for j in range(len(array_j), 0, -1):
    #         to_print += str(array_to_calc[i - 1][j - 1]) + " "
    #     print(to_print)




def pretty_print_approach2(columns, rows, lcs_array):
    for i in range(1, len(rows) + 1):
        i = i - 1
        to_print = ""
        for j in range(1, len(columns) + 1):
            j = j - 1
            to_print += str(lcs_array[i][j]) + " "
        print(to_print)


def lcs(x, y):
    """Clever solution"""
    if len(x) == 0 or len(y) == 0:
        return ''
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        lcs1 = lcs(x,y[:-1])
        lcs2 = lcs(x[:-1],y)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2

if __name__ == "__main__":
    # str1 = str(input("String 1 please:"))
    # str2 = str(input("String 2 please:"))
    str2 = "ABCBDAB"
    str1 = "BDCAB"

    str1 = "132535365"
    str2 ="123456789"
    #
    # str2 = "AGGTAB"
    # str1 = "GXTXAYB"

    # str1 = "a"
    # str2 = "b"

    i, j, _array = ini_array_aproach2(str1, str2)


    # calc_lcs_approach2(i, j, _array)
    # pretty_print(_array)

    print(lcs(str1, str2))