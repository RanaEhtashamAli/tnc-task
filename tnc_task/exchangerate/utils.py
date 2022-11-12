import requests
from django.conf import settings


def format_exchange_data(data):
    data = data['Realtime Currency Exchange Rate']
    return {key.split('. ')[1].replace(' ', '_').lower(): value for key, value in data.items()}



def get_exchange_rate():
    url = f'{settings.ALPHA_VANTAGE_API_BASE_URL}/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={settings.ALPHA_VANTAGE_API_KEY}'
    r = requests.get(url)
    data = format_exchange_data(r.json())
    return data
