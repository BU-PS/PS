import unittest


def solution(s: str):
    _s = sorted([ord(s) for s in s], reverse=True)
    return "".join(chr(i) for i in _s)


def selection_sort_solution(s: str):
    """
    배열을 처음 인덱스 부터 돌면서 가장 작은 수의 위치 값과 변경
    :param s: string
    :return: string
    """
    s = list(s)
    s_len = len(s)
    for index in range(s_len):
        min_index = index
        for idx in range(index + 1, s_len):
            if ord(s[index]) > ord(s[idx]):
                min_index = idx
        s[index], s[min_index] = s[min_index], s[index]

    return "".join(s[::-1])


def bubble_sort_solution(s: str):
    """
    처음 인덱스 부터 다음 인덱스와 계속 비교 하면서 위치 변경
    :param s: string
    :return: string
    """
    s = list(s)
    s_len = len(s)
    for index in range(s_len):
        for idx in range(index + 1, s_len):
            if ord(s[index]) > ord(s[idx]):
                s[index], s[idx] = s[idx], s[index]
    return "".join(s[::-1])


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._random_string = "Zbcdefg"
        self._result = "gfedcbZ"

    def test_solution(self):
        result = solution(s=self._random_string)
        self.assertEqual(self._result, result)

    def test_selection_sort(self):
        result = selection_sort_solution(s=self._random_string)
        self.assertEqual(self._result, result)

    def test_bubble_sort(self):
        result = bubble_sort_solution(s=self._random_string)
        self.assertEqual(self._result, result)


if __name__ == '__main__':
    unittest.main()
