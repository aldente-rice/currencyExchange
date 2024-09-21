from bs4 import BeautifulSoup
import requests
import datetime


# def exchangeCurrency(currency_from = "USD", currency_to = "", amount_from = 0, amount_to = 0):
html_text = requests.get('https://markets.businessinsider.com/currencies').text
soup = BeautifulSoup(html_text, 'lxml')


# fills in currency_list.txt for all the available currencies to exchange to/from
def fill_currency_list(currency):
    f = open('currency_list.txt', 'w')
    currency_containers = soup.find_all('tr', class_='row-hover')  # all containers that contain currency info.

    for currency_container in currency_containers:
        symbol = currency_container.find('a', class_='font-color-black')
        f.write(symbol.text[len(currency) + 1:] + ' | ')
        search_container = currency_container.find_all('td', class_='table__td text-right')
        f.write(search_container[1].text.strip() + ' | ')
        f.write(search_container[4].text.strip() + '\n')

    f.close()


fill_currency_list('usd')
print('Last Updated: ')

'''
if __name__ == '__main__':
    info = input("Enter currency and update interval (in minutes): ")
    info_split = info.split()
    fill_currency_list(info_split[0], info_split[1])
'''











''' the old way where find each column at a time, rather than stay in row and collect info.

    for currency_symbol in currency_symbols:
        currency_rate = currency_symbol.find_all('td', class_='table__td text-right')
        for index, rate in enumerate(currency_rate):
            currency_name = rate.find('a')
            if currency_name:
                print(currency_name.text.strip())

    for currency_symbol in currency_symbols:
        a = currency_symbol.find('a', class_='font-color-black')
        curr_currency = currency  # user's input currency to convert from
        if a:
            print(a.text[len(curr_currency) + 1:])

    for currency_symbol in currency_symbols:
        currency_rate = currency_symbol.find_all('td', class_='table__td text-right')
        for index, rate in enumerate(currency_rate):
            if index % 4 == 0 and index != 0:
                print(rate.text.strip())


    f.write(f'{currency_symbol} | {currency_name} | {currency_rate}\n')'''



'''  finds each currency name
currency_symbols = soup.find_all('tr', class_='row-hover')
for currency_symbol in currency_symbols:
    currency_rate = currency_symbol.find_all('td', class_='table__td text-right')
    for index, rate in enumerate(currency_rate):
        currency_name = rate.find('a')
        if currency_name:
            print(currency_name.text.strip())
'''



''' finds each currency symbol
currency_symbols = soup.find_all('tr', class_='row-hover')
for currency_symbol in currency_symbols:
    a = currency_symbol.find('a', class_='font-color-black')
    curr_currency = 'USD'  # user's input currency to convert from
    if a:
        print(a.text[len(curr_currency) + 1:])
'''


''' finds each currency amount relative to user's currency
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