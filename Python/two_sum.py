# def find_two_sum(numbers, target_sum):
#     """
#     :param numbers: (list of ints) The list of numbers.
#     :param target_sum: (int) The required target sum.
#     :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
#     """
#     memory = set()
#
#     for i, val in enumerate(numbers):
#         if target_sum - val in memory:
#             return i, numbers.index(target_sum - val)
#         memory.add(target_sum - val)
#     return None


def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    mem = {}

    for i, val in enumerate(numbers):
        if target_sum - val in mem:
            return (i, mem[target_sum - val])
        mem[val] = i
    return None


if __name__ == "__main__":
    # print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
    print(find_two_sum([5, 1, 5, 7, 5, 9], 10))
    # print(find_two_sum([3, 1, 3, 6, 2, 90], 10))