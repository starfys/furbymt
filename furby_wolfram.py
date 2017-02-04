import requests

def wolfram(my_in):
    my_in.replace(" ", "+")
    print(my_in)
    r = requests.get('http://api.wolframalpha.com/v1/spoken?appid=E2HWYP-L9U5YA5H73&i={}%3f'.format(my_in))
    string = r.text
    return string
