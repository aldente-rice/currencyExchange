from bs4 import BeautifulSoup
import requests

def exchangeCurrency():
    html_text = requests.get('https://markets.businessinsider.com/currencies').text
    soup = BeautifulSoup(html_text, 'lxml')


