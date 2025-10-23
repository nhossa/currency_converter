import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_Key = os.getenv("API_KEY")

BASE_URL= f'https://api.freecurrencyapi.com/v1/latest?apikey={API_Key}'

CURRENCIES = "USD,EUR,GBP,INR,AUD,CAD,SGD,JPY,CHF,CNY".split(',')

def convert_currency(base):
    currencies = (",").join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        print(data)
        print(type(data))
        return data['data']

    
    except Exception as e:
        print(e)
        return None

while True:

    input_currency = input("Enter base currency (q for quit): ").upper()
    if input_currency == 'Q':
        break
    if input_currency not in CURRENCIES:
        print(f"Invalid currency code. Please enter a valid currency from the list:{CURRENCIES}")
        continue

    

    data = convert_currency(input_currency)
    del data[input_currency]  # Remove base currency from the results
    for ticker,value in data.items():
        print(f"{ticker}: {value}")


