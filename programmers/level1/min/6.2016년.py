# 요일을 리턴
# 구할 수 있는 방법 생각하기
# 가장 쉽게 라이브러리를 이용하여 해보기


import unittest


def solution(month: int, day: int) -> str:
    import calendar
    answer = {
        0: "MON",
        1: "TUE",
        2: "WED",
        3: "THU",
        4: "FRI",
        5: "SAT",
        6: "SUN"
    }
    day = calendar.weekday(year=2016, month=month, day=day)
    return answer[day]


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._month = 5
        self._day = 24
        self._result = "TUE"

    def test_solution(self):
        result = solution(month=self._month, day=self._day)
        self.assertEqual(self._result, result)


if __name__ == '__main__':
    unittest.main()