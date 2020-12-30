def solution(arr, divisor):
    answer = [data for data in arr if data / divisor % 1 == 0]
    
    if not answer:
        return [-1]
        
    return sorted(answer)