def solution(s):
    min_zip_length = len(s)  # 최소길이 (최소 길이는 적어도 주어진 문자열 길이를 넘어가지 않음)

    # 문자열 길이가 N일 때, 길이가 N/2 보다 크게 잘랐을 때는 길이가 줄지 않음 (절반만 탐색해도 됨)
    # 따라서 1 ~ N/2 길이로 자르는 방법을 모두 탐색한 후 그중 가장 짧은 방법을 선택하면 됩니다.
    for index in range(1, len(s) // 2 + 1):
        zip_str = ''                # 압축한 문자열
        compare_str = s[0:index]    # 비교 문자열
        zip_count = 1               # 압축 횟수

        # 문자 비교 - index 개의 글자씩 잘라서 비교 
        for j in range(index, len(s) + 1, index):
            if compare_str == s[j:j + index]:  # 압축 문자와 비교 문자가 같으면 압축 횟수 증가, (범위를 넘어가는 경우 '' 빈 문자임.)
                zip_count += 1
            else:  # 그렇지 않으면 즉, 같은 문자가 아닌 경우,
                zip_str += f"{zip_count if zip_count > 1 else ''}{compare_str}"  # 여러 번 압축된 경우 해당 압축 횟수 쓰고 문자열 작성, 아니면 해당 문자 작성
                compare_str = s[j:j + index]    # 비교 문자열 재 할당
                zip_count = 1

        # 마지막 비교 문자열을 더해준다 🤩
        zip_str += compare_str

        # 최소 길이 update
        if min_zip_length > len(zip_str):
            min_zip_length = len(zip_str)

    return min_zip_length