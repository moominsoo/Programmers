def solution(hp): #이거 그리디?
    answer=0
    for i in range(hp):
        if hp>=5:
            answer += hp//5
            hp = hp%5
        elif hp<5 and hp>=3:
            answer += hp //3
            hp = hp%3
        elif hp<3 and hp>=1:
            answer += hp//1
            hp = hp%1
        else:
            answer+=0
            
    return answer