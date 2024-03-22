def solution(money):
    return [money//5500,money-(5500*(money//5500))] #이거 결국 [money//5500, money%5500]이랑 같은거
