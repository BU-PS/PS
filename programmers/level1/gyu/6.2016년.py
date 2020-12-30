def solution(month, day):
    day_word = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    day = sum(days[:month]) + day - 1   # 인덱스는 0부터 시작
    day %= 7                            # 요일 단위
    
    return  day_word[day]    