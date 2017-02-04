def math(strfull):

    num1 = int(strfull.split()[0])
    sign = strfull.split()[1]
    num2 = int(strfull.split()[2])
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

