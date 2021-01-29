def solution(progresses, speeds):
    answer = []
    
    while progresses:
        count = 0
        idx = 0
        
        # 각 날마다 증가         
        for i in range(len(progresses)):        
            progresses[i] += speeds[i]
        
        # 진행속도 검사         
        while progresses and progresses[0] >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
            
        if count:
            answer.append(count)
        
    return answer