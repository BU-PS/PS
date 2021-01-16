def solution(N, stages):
    denominator = len(stages)       # 분모
    failure = []                    # 실패율
    
    # 실패율 구하기
    for i in range(1, N+1):
        if denominator == 0:                        # 분모가 0 인경우 이후 부터는 다 0
            failure.append((i, 0))    
            continue
            
        count = stages.count(i)
        failure.append((i, count / denominator))    # i는 몇번째인지 확인
        denominator -= count
    
    # 실패율이 높은 스테이지부터 내림차순
    failure.sort(key=lambda x:x[1], reverse=True)
    
    return [fail[0] for fail in failure]