# 뒤에있는 주식가격들과 비교해 가격이 몇초간 유지되는지 비교
# 예시를 보면, 1은 쭉 유지되고 2도 쭉 유지되고 3은 뒤가 2이니 1초후 떨어지고 2는 쭉 유지되고 3은 뒤에 숫자가 없길래 유지됨.
def solution(prices):
    answer = [0 for i in range(len(prices))] # return값을 담을 배열
    for i in range(len(prices)): 
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]:
                answer[i]+=1
            else: 
                answer[i]+=1 
                break
    return answer