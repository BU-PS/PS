def solution(arr,divisor):
    answer=[arr[i] for i in range(len(arr)) if arr[i]%divisor==0]
    if len(answer)>0:
        return sorted(answer)
    return [-1]