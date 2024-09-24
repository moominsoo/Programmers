def solution(n):
    m=[]
    for i in range(n,0,-1):
        if n%i ==0:
            m.append(i)
            m.append(n//i)
    m1= list(set(m)) #중복제거
    return sum(m1)