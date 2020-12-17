def solution(x):
    answer=[int(i) for i in str(x)]
    return x%sum(answer)==0