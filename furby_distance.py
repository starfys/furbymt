import requests

def distance(loc1, loc2):

    req = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins=" +  loc1 + "&destinations=" + loc2)
    json_soup = req.json()
    return(str(json_soup['rows'][0]['elements'][0]['distance']['text'] + ' between ' + json_soup['origin_addresses'][0] + ' and '+ json_soup['destination_addresses'][0]))