from functools import reduce


def count_positives_sum_negatives(arr):
    if not arr:
        return []
    arr = [len(list(filter(lambda x: x > 0, arr))), reduce(lambda x, y: x + y, filter(lambda x: x < 0, arr), 0)]
    return arr


def invert(arr):
    arr = list(map(lambda x: x * -1, arr))
    return arr


def series_num(n):
    def series_sum(n):
        if not n:
            return '0.00'
        return '{:.2f}'.format(1 + sum([1 / x for x in range(4, n * 3 + 1, 3)]))


def solution1(digits):
    a = max(digits[a:a + 5] for a in range(len(digits) - 4))
    return int(a)


def solution2(digits):
    inc = 0
    _len = len(digits)
    greater = int()
    number = int(s[inc: inc + 5])
    while inc + 6 <= _len + 1:
        if number > greater:
            greater = number

        number = int(s[inc + 1: inc + 6])
        inc += 1

    return greater


def dig_pow(n, p):
    v = sum([int(v) ** (p + i) for i, v in enumerate(str(n))])
    k = v / n
    if k == int(k):
        return int(k)
    return -1


def my_fibonacci(n, _list):
    """
    n = 4 => 3
    n = 3 => 2
    n = 2 => 1
    n = 1 => 1
    :param n: int
    :return: int
    """
    if n <= 1:
        return n
    op1 = my_fibonacci(n - 2, _list)
    op2 = my_fibonacci(n - 1, _list)
    _list.append(op1 + op2)
    return op1 + op2


def perimeter(n):
    n += 1
    perimeters = []
    cache = {}
    def fibo(nth):

        if nth in cache:
            return cache[nth]

        if nth <= 1:
            return nth

        op1 = fibo(nth - 2)
        op2 = fibo(nth - 1)
        calc = op1 + op2
        cache[n] = calc
        perimeters.append(calc)

        return calc
    fibo(n)
    perimeters.insert(0, 1)
    perimeters = perimeters[-n:]
    return perimeters
    # perimeters.insert(0, 1)
    # return sum(perimeters)*4

def permiter_soft(n):
    prev = 0
    current = 1
    if n == 1:
        return 4 * 1
    else:
        op1 = 1
        op2 = 1
        fib = [op1, op2]
        ac = 0
        for x in range(n - 1):
            f = op1 + op2
            fib.append(f)
            ac += (4 * f)
            op1 = op2
            op2 = f
        return fib, ac + 8

if __name__ =='__main__':
    # Output must be: , [10, -65]
    # count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
    # count_positives_sum_negatives([1])

    # invert_i1 = [1, 2, 3, 4, 5]
    # invert(invert_i1)
    # invert_i2 = [1,-2,3,-4,5]
    # invert(invert_i2)
    # invert_i3 = []
    # invert(invert_i3)
    # series_num(1)
    # s = "7316717653133062491922511967442657474235534919493496983520368542506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753123457977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257540920752963450"
    s = '1234567898765'
    s = '12345'
    # s = '731674765'
    # print(solution1(s))
    # print(solution2(s))

    # print(dig_pow(695, 2))
    # print(dig_pow(46288, 3))
    # print(perimeter(50))
    print(permiter_soft(30))