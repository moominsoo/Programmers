def solution(n):
    rest=[]
    for x in range(1,n+1):
        if n%x==1:
            rest.append(x)
    answer = min(rest)  
    return answer