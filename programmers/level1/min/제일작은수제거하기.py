# 1. 배열 내 가장 작은 수 찾기 -> min 내장 함수 사용 or 정렬 후 가장 작은 수 뽑기 or heap 사용 ?
# 2. 조건에 따라 실행


def solution(arr: list):
    if arr is None or len(arr) == 1:
        return [-1]

    min_value = min(arr)
    for index, value in enumerate(arr):
        if value == min_value:
            del arr[index]
    return arr
