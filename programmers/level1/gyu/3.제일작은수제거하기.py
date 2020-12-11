def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    _min = min(arr)
    return [data for data in arr if data > _min]