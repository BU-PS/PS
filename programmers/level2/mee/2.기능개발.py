def solution(progresses,speeds):
    answer=[]

    while progresses:
        count=0
        progresses=[i+j for i,j in zip(progresses,speeds)]

        while progresses and progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            count+=1
        
        if count:
            answer.append(count)
            
    return answer