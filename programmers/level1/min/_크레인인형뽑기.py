# 배열을 피벗 할까 말까?
# 피벗한다면 해당 리스트들을 가지고 처리 가능
# 피벗하지 않는 다면 현재 리스트로 처리
# 1. list.pop
# 2. list insert
# 1,2 를 실행하기 전에 이전 데이터를 가지고있고 다음것과 동일하다면 삭제하고 넣는건 어떨까



import unittest


def solution(boards: list, moves: list) -> int:
    answer = 0
    past = [None]
    pivots = {index: list() for index in range(1, len(boards) + 1)}

    for index, board in enumerate(boards, start=1):
        for idx, value in enumerate(board, start=1):
            if value != 0:
                pivots[idx].append(value)

    for key, value in pivots.items():
        pivots[key] = value[::-1]

    for move in moves:
        try:
            pick = pivots[move].pop()

            if past[-1] == pick:
                past.pop()
                answer += 2
            else:
                past.append(pick)
        except IndexError:
            continue
    return answer


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
        self._move = [1, 5, 3, 5, 1, 2, 1, 4]
        self._result = 4

    def test_solution(self):
        solution(self._board, self._move)


if __name__ == '__main__':
    unittest.main()


# [[0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 3],
#  [0, 2, 5, 0, 1],
#  [4, 2, 4, 4, 2],
#  [3, 5, 1, 3, 1]]