

def solution(arr1, arr2) -> list:
    answer = list()
    for ar1, ar2 in zip(arr1, arr2):
        outer_list = list()
        for a1, a2 in zip(ar1, ar2):
            outer_list.append(a1+a2)
        answer.append(outer_list)
    return answer