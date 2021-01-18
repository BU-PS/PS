def solution(n, arr1, arr2):
    answer = []
    temp1 = []
    temp2 = []
    
    # arr1 2진수로 변환
    for arr in arr1:
        binary = format(arr, 'b')
        if len(binary) < n:
            binary = '0' * (n - len(binary)) + binary
        
        temp1.append(binary)

    # arr2 2진수로 변환
    for arr in arr2:
        binary = format(arr, 'b')
        if len(binary) < n:
            binary = '0' * (n - len(binary)) + binary
        
        temp2.append(binary)
    
    
    # or 연산 수행 후 답 도출
    for i in range(n):
        temp = ''
        for j in range(n):
            temp += str(eval(temp1[i][j]) or temp2[i][j])
        temp = temp.replace("1", "#").replace("0", " ")
        answer.append(temp)

    return answer

''' 참고하기
def solution(n, arr1, arr2):
    answer = []
    for index in range(0,n):
        answer.append(str(bin(arr1[index] | arr2[index] | pow(2,n))).replace("0b1","").replace("1","#").replace("0"," "))

    return answer
'''