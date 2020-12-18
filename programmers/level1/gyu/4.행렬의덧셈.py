def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1


def solution(arr1, arr2):
    column, row = len(arr1), len(arr1[0])

    answer = [[0 for _ in range(row)] for _ in range(column)]
                  
    for c in range(column):
        for r in range(row):
            answer[c][r] = arr1[c][r] + arr2[c][r]

    return answer