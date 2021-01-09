# 그냥 있어보일려고 한줄로 축약 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
def solution(numbers):
    return sorted(list(set([numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(i+1, len(numbers))])))


# 가독성 좋은게 최고야~
def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):        
            answer.append(numbers[i] + numbers[j])
        
    answer = list(set(answer))      # sort후 set 을 적용하면 set 은 정렬된 순서를 보장하지 않음. 따라서 set 하고 sort 해줘야함.
    answer.sort()
    return answer