# arr값 각각 2진수로 만들기
# arr1과 arr2 합치기
# 합친 값에서 1인곳은 #으로 0인곳은 공백으로 표현하여 리턴
def solution(n, arr1, arr2):
    answer=[] 
    for i in range(n):
        arr=bin(arr1[i] | arr2[i]) # arr1과 arr2를 2진수로 만들어서 합쳐주기(비트연산자)
        arr=arr[2:] 

        if len(arr)<n:
            arr='0'*(n-len(arr))+arr #잊어버리지말기..
        arr=arr.replace('0',' ').replace('1','#')
        answer.append(arr)
        
    return answer