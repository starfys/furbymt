def get_time():
    from time import gmtime, strftime
    string = strftime("%l:%M")
    return string