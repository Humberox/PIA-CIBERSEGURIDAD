import requests
import getpass
import json

#API = getpass.getpass("Ingresa tu api key: ")
def VirusTotal(API, SITIO):
    URL = 'https://www.virustotal.com/vtapi/v2/url/report'

    #Sitio = "https://webzel.net/koko//wechat1.zip"

    params = {'apikey': API, 'resource': SITIO}
    response = requests.get(URL, params=params)
    respjson = json.loads(response.content)

    if respjson['positives'] <= 0:
        print('\n EL SITIO NO ES PELIGROSO ')

    elif 1 >= respjson['positives'] >= 3:
        print('\n EL SITIO PPSIBLEMENTE SEA PELIGROSO ')

    elif respjson['positives'] >= 4:
        print('\n EL SITIO ES PELIGROSO ')

    else:
        print('\n EL SITIO NO EXISTE ')
