def solution(n):
    n = str(n)
    sum=0
    for i in n:
        sum += int(i)
    return sum

#sum(int(i) for i in str(n)) 컴프리헨션 연습
