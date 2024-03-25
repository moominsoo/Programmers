def solution(s1, s2):
    s3 = [x for x in s1 if x not in s2]
    return len(s1)-len(s3)