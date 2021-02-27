import unittest

"""
아이디의 길이는 3자 이상 15자 이하여야 합니다.
아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

"""
import re


def solution(new_id: str) -> str:
    """
    recommended new id base input id
    :param new_id: new id
    :return: string
    """
    pattern = "[0-9a-z-_.]"

    answer = [
        string if string.islower() else string.lower() for string in new_id
    ]

    answer = [
        string for string in answer if re.match(pattern=pattern, string=string)
    ]

    comma_count = answer.count(".")

    string_answer = "".join(answer)

    for i in range(comma_count, 1, -1):
        string_answer = string_answer.replace("." * i, ".")

    if string_answer.startswith("."):
        string_answer = string_answer[1:]
    if string_answer.endswith("."):
        string_answer = string_answer[:-1]

    if not string_answer:
        string_answer = "a"

    if len(string_answer) >= 16:
        string_answer = string_answer[:15]
        if string_answer.endswith("."):
            string_answer = string_answer[:14]

    if len(string_answer) <= 2:
        if len(string_answer) == 1:
            string_answer = string_answer * 3
        if len(string_answer) == 2:
            string_answer = string_answer[0] + string_answer[1] * 2

    return string_answer


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        # self._new_id = "...!@BaT#*..y.abcdefghijklm"
        self._new_id = "=.="
        self._result = "aaa"

    def test_solution(self):
        result = solution(new_id=self._new_id)
        self.assertEqual(self._result, result)

if __name__ == '__main__':
    unittest.main()

