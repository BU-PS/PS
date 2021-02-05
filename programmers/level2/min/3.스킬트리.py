import  unittest


def solution(skill: str, skill_trees: list) -> int:
    answer = 0
    results = list()

    # 스킬 인덱스 지정해주자
    skill_index = {
        s: str(index)
        for index, s in enumerate(skill, start=1)
    }

    # 스킬 돌면서 인덱스값이 있는 리스트로 바꾸자
    for skill_tree in skill_trees:
        result = ""
        for s in skill_tree:
            idx = skill_index.get(s)

            if idx is not None:
                result += idx
        results.append(result)

    # 스킬 인덱스만 뽑아 가져오기
    skill_indexs = list(skill_index.values())

    # 스킬 인덱스 값을 슬라이스 하여 result의 값과 묶어서 같은 경우에만 값을 추가
    for result in results:
        result_length = len(result)
        count = 0
        for idx, res in zip(skill_indexs[:result_length], result):
            if idx == res:
                count += 1

        if count == result_length:
            answer += 1

    # 리턴
    return answer


class solutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._skill = "CBD"
        self._skill_tree = ["BACDE", "CBADF", "AECB", "BDA"]
        self._result = 2

    def test_solution(self):
        result = solution(skill=self._skill, skill_trees=self._skill_tree)
        self.assertEqual(self._result, result)


if __name__ == '__main__':
    unittest.main()