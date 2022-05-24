from urllib import response
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style
import sys
import os

def get_price():
    response = requests.get(url)

    soup = BeautifulSoup(response.content,'html.parser')

    if asset == 'btc':
        price = soup.find('span',{'class':'price'}).text
    else:
        price = soup.find('span',{'class':'woobJfK-Xb2EM1W1o8yoE'}).text
    return float(price.replace(",",""))

asset = input('Abbreviation of the assets: ')
url = 'https://cryptowat.ch/assets/' + asset

try:
    price = get_price()

except AttributeError:
    print("The asset doesn't exist or it's not supported!")
    sys.exit()

if sys.platform == 'win32':
    os.system('cls')
else:
    os.system('clear')


price = 0


while True:
    last_price = price
    price = get_price()

    if price > last_price:
        color = Fore.GREEN
    elif last_price > price:
        color = Fore.RED
    else:
        color = Style.RESET_ALL

    print('$',end='')
    print(color + str(price) + Style.RESET_ALL)