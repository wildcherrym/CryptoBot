import requests
import json
from config import keys
class ConvertionException(Exception):
    pass
class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалость обработать количество {amount}')
        r = requests.get(f'https://v6.exchangerate-api.com/v6/e474815cdf33212a41be97ec/pair/{base_ticker}/{quote_ticker}/{amount}')
        result = json.loads(r.content)
        if result['result']!='success':
            raise ConvertionException('Ошибка при получении курса валют.')
        total_base = result['conversion_result']
        return total_base