from flask import Blueprint, render_template
import requests
from quickchart import QuickChart

stock = Blueprint('stock', __name__, url_prefix='/stock')



API_URL = 'https://financialmodelingprep.com/api/v3/quote-short/{symbol}'

def fetch_price(symbol):
    data = requests.get(API_URL.format(symbol=symbol),
                                params={"apikey" : {API_KEY}}).json()
    print(data)
    for item in data:
        price = item['price']
        return price

def fetch_income(symbol):
    url = 'https://financialmodelingprep.com/api/v3/income-statement/{symbol}'
    financials = requests.get(url.format(symbol=symbol), params={"limit":120, "apikey" : {API_KEY} }).json()
    financials.sort(key=lambda quarter: quarter["date"])
    # print(financials)
    return financials

@stock.route('/<string:symbol>')
def quote(symbol):
    price = fetch_price(symbol)
    return render_template('stock/quote.html', symbol=symbol, stock_price=price )

@stock.route('/<string:symbol>/financials')
def financials(symbol):
    data = fetch_income(symbol)
    chart_data = [float(q["eps"]) for q in data if q["eps"]]
    chart_params = { "type": 'line',
                     "data": {
                        'labels': [q["date"] for q in data if q["eps"]],
                        'datasets': [{'label': 'Earnings Per Share (EPS)', 'data': chart_data }]
                    }}


    return render_template('stock/financials.html', symbol=symbol, financials=data, chart_params=chart_params)
