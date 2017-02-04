def math(num1, sign, num2):
    if sign == '+':
        string = str(num1+num2)
    elif sign == '-':
        string = str(num1-num2)
    elif sign == '*':
        string = str(num1*num2)
    elif sign == '/':
        string = str(num1/num2)
    else:
        string = "Error!"

    return string

