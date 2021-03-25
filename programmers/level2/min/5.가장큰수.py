import unittest


def solution(numbers: list):
    if sum(numbers) == 0:
        return '0'
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x * 3, reverse=True)
    return ''.join(str_numbers)


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._numbers = [6, 10, 2]

    def test_solution(self):
        solution(numbers=self._numbers)
