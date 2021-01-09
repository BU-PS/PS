def solution(numbers):
    answer=[numbers[i]+numbers[j] for j in range(i+1,len(numbers)) for i in range(len(numbers))]
    return sorted(set(answer))