def solution(n):
    pizza= int(n/7)
    if (n%7) !=0:
        pizza+=1
    return pizza