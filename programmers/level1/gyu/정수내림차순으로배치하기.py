# log8000000000 -> 33 정도?
def solution(n):
    n = [i for i in str(n)]
    n.sort(reverse=True)
    return int("".join(n))

''' 틀린 코드 - 시간복잡도... O(N^2)??
# * 연산자의 시간복잡도는 뭐지?
def solution(n):
    answer = ''
    array = [0] * 10
    n = [int(i) for i in str(n)]

    for i in n:
        array[i] += 1

    for i in range(9, 0, -1):
        if array[i]:
            answer += str(i) * array[i]

    return int(answer)
'''
