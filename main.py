"""
Module contains helper methods to get financial data
"""
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup

GOOGLE_FINANCE_URL = 'https://www.google.com/finance/info?q='


def get_stock_price(stock):
    """
    Gets stock price
    """
    page = urlopen(GOOGLE_FINANCE_URL + stock)
    soup = BeautifulSoup(page, "lxml")
    response_string = soup.body.string
    stock_string = response_string[2:]
    stock_string_length = len(stock_string)
    stock_object = stock_string[2:stock_string_length - 2]
    stock_json = json.loads(stock_object)
    print(stock_json['l'])


get_stock_price('GOOG')