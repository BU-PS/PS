def solution(prices):
    answer = [0] * len(prices)
    end = len(prices)
    
    for i in range(end):
        count = 1
        for j in range(i+1, end):
            if prices[j] < prices[i]:
                answer[i] = count
                break
            if j == end-1:
                answer[i] = count
            count += 1
            
    return answer