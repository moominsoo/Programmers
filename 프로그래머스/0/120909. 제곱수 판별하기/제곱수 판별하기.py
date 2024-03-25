def solution(n):
    measure=0 #약수개수
    for i in range(1,n+1):
        if n%i==0:
            measure+=1 
    if measure%2==0:
        answer=2
    else:
        answer=1
    return answer