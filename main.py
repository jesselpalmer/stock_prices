"""
Module contains helper methods to get financial data
"""
import json
import requests

class Company:
  YAHOO_FINANCE_URL_BASE = 'https://query1.finance.yahoo.com/v8/finance/chart/'
  symbol = ""
  _company_raw_json_data = {}

  def __init__(self, symbol):
    self.symbol = symbol.upper()
    self._company_raw_json_data = requests.get(self.YAHOO_FINANCE_URL_BASE + self.symbol).json()


google = Company('GOOG')
print(google._company_raw_json_data)