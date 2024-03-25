def solution(s1, s2):
    s3 = [x for x in s1 if x not in s2]
    return len(s1)-len(s3)

#return len([x for x in s1 if x in s2]) not in 말고in 해도됨. 리스트 컴프리헨션
#set 이용하여 푸는 방법(
