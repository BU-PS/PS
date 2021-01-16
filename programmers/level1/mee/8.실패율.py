def solution(N, stages):
    answer = [stages.count(i) for i in range(1,N+1)] # stage당 실패수
    fail_p=[0 for i in range(N)] # 실패율을 담을 배열
    person=len(stages)  # 총 남은인원(분모)
    for i in range(N):
        if person==0:  #분모가 0이라면, [i,0]을 담아줌
            fail_p[i]=[i,0]
            continue
        fail_p[i]=[i,(answer[i]/person)] #분모가 0이 아니라면, [i,몫을 담아줌]
        person=person-answer[i] # 인원을 빼줌
    
    fail_p.sort(key=lambda x:x[1], reverse=True) # 몫을 기준으로 정렬
    return [fail_p[j][0]+1 for j in range(len(fail_p))]