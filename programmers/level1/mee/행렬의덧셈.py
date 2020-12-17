def solution(arr1,arr2):
    answer=[]
    for i,j in zip(arr1,arr2):
        sum=[]
        for k,l in zip(i,j):
            sum.append(k+l)
        answer.append(sum)
    return answer

    #answer=[[k+l for k,l in zip(i,j)]for i,j in zip(arr1,arr2)]