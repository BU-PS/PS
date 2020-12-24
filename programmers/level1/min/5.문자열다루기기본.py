import unittest


def solution(strings: str) -> bool:
    if len(strings) not in [4, 6]:
        return False
    for s in strings:
        try:
            int(s)
        except ValueError:
            return False
    return True


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._first_strings = "1234"
        self._second_strings = "asd2"

    def test_solution(self):
        result = solution(strings=self._first_strings)
        self.assertEqual(True, result)
        result = solution(strings=self._second_strings)
        self.assertEqual(False, result)


if __name__ == '__main__':
    unittest.main()