from Python.math_problems.count_positive_negatives import (count_positives_sum_negatives,
                                                           invert)


def test_count_positives_sum_negatives():
    _input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    result = [10, -65]
    assert count_positives_sum_negatives(_input) == result

    _input = [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]
    result = [8, -50]

    assert count_positives_sum_negatives(_input) == result

    _input = [1]
    result = [1, 0]

    assert count_positives_sum_negatives(_input) == result



