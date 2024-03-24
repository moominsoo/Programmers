def solution(number, n, m):
    if number%n==0 and number%m==0:
        answer=1
    else:
        answer=0
        
    return answer
#return 1 if number%n==0 and number%m==0 else 0