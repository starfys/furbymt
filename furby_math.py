def math(num1, sign, num2):
    if sign == '+':
        string = string(num1+num2)
    if sign == '-':
        string = string(num1-num2)
    if sign == '*':
        string = string(num1*num2)
    if sign == '/':
        string = string(num1/num2)
    else:
        string = "Error!"

    return string

