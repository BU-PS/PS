def solution(array, commands):
    answer = []
    
    for start, end, k in commands:
        tmp = array[start-1:end]
        answer.append(sorted(tmp)[k-1])
        
    return answer