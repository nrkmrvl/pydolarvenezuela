from bs4 import BeautifulSoup # pip i bs4
import requests # pip i requests
import urllib3

# Desactiva advertencia por problemas de SSL en la página
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 

def price():
    webSite = "https://monitordolarvenezuela.com/"
    webResult = requests.get(webSite)
    dataWeb = BeautifulSoup(webResult.content, 'html.parser')
    divElements = dataWeb.find_all('div', 'col-12 col-sm-4 col-md-2 col-lg-2')
    priceResult = []
    for divElement in divElements:
        text = divElement.find('p')
        priceResult.append(text.text.split(' ')[-1].replace(',', '.'))
    return {
        '$bcv' : f'Bs. {priceResult[0]}',
        '$enparalelovzla' : f'Bs. {priceResult[1]}',
        '$dolartoday' : f'Bs. {priceResult[2]}',
        '$monitordolarweb' : f'Bs. {priceResult[3]}',
        '$enparalelovzlavip' : f'Bs. {priceResult[4]}',
        '$binancep2p' : f'Bs. {priceResult[5]}'
    }

# Call the price() function to get the price result
priceResult = price()

# Now you can print the price result
for key, value in priceResult.items():
    print(key, value)