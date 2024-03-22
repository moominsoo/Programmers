def solution(str1, str2):
    if str2 in str1:
        return 1
    return 2

# return 1 + int(str2 not in str1) 기본 1 반환, 없을때 +1
# return 1 if str2 in str1 else 2
