def math(num1, sign, num2):
    if sign == '+':
        string = str(num1+num2)
    elif sign == '-':
        string = str(num1-num2)
    elif sign == '*':
        string = str(num1*num2)
    elif sign == '/':
>>>>>>> 5d32cd56e6622064042a2d259f4b61b9e4894527
        string = str(num1/num2)
    else:
        string = "Error!"

    return string

