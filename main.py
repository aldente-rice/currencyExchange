from bs4 import BeautifulSoup
import requests


# def exchangeCurrency(currency_from = "USD", currency_to = "", amount_from = 0, amount_to = 0):
html_text = requests.get('https://markets.businessinsider.com/currencies').text
soup = BeautifulSoup(html_text, 'lxml')


# fills in currency_list.txt for all the available currencies to exchange to/from
def fill_currency_list():
    currency_symbol = soup.find_all('td', class_='table__td bold')
    currency_name = soup.find_all()
    currency_rate = soup.find_all()

    for currency in currency_symbol:
        with open('currency_list.txt', 'w') as f:
            f.write(f'{currency_symbol} | {currency_name} | {currency_rate}\n')

''' finds each currency name
currency_symbols = soup.find_all('td', class_='table__td text-right')
for currency_symbol in currency_symbols:
    currency_name = currency_symbol.find('a')
    if currency_name:
        print(currency_name.text)
'''
'''
currency_symbols = soup.find_all('tr', class_='row-hover')
for currency_symbol in currency_symbols:
    a = currency_symbol.find('a', class_='font-color-black')
    curr_currency = 'USD'  # user's input currency to convert from
    if a:
        print(a.text[len(curr_currency) + 1:])
'''

'''
currency_symbols = soup.find_all('tr', class_='row-hover')
for currency_symbol in currency_symbols:
    currency_rate = currency_symbol.find_all('td', class_='table__td text-right')
    for index, rate in enumerate(currency_rate):
        if index % 4 == 0 and index != 0:
            print(rate.text.strip())
'''






'''
currency_table = soup.find(id='currency_container_table')
# currency_table = soup.find('tbody', clsss_='table__tbody').text


# print(currency_table.prettify()) adds indents to html to make it pretty

start_currency = input('Enter Starting Currency and Amount (i.e. USD 100): ')
parse_start_currency = start_currency.split()  # format: ['currency', amount]




end_currency = input('Enter Currency to Convert to (i.e. CNY): ')
converted_amount = 0
time_date = 0  # updates currency rates every 10 minutes

print(f'{start_currency.upper()} -> {end_currency} {converted_amount}')
print(f'Converted from [{parse_start_currency[0].upper()}] to [{end_currency.upper()}] updated as of [{time_date}]')
'''