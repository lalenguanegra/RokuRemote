import requests

def keypress(url, key):
    request_url = url + '/keypress/' + key
    requests.post(request_url)

keypress('http://192.168.0.21:8060', 'poweron')