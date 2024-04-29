def solution(my_string, num1, num2):
    my=my_string
    return my[:num1]+my[num2:num2+1]+my[num1+1:num2]+my[num1:num1+1]+my[num2+1:]