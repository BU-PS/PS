def solution(arr):
    answer=[j for i,j in enumerate(arr) if arr[i]!=arr[i-1] or i==0]
    return answer
