def get_time():
    from time import gmtime, strftime
    string = strftime("%l:%M %p")
    if (strftime("%l") == 12) and (strftime("%l") == "am") and (strftime("%M") == 00):
        return "It's high noon!"
    if (strftime("%M") == 00):
        return(strftime("%l") + " o'clock")
    else:
        return string
