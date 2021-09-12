from math import isqrt
from os import read, write
from typing import Generator
from pandas.core.frame import DataFrame
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '02c65827-46a1-4766-86fc-c9833d6a3462',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    df = DataFrame(data["data"])
    writer=pd.ExcelWriter("bitcoinEXL.xlsx")
    df.to_excel(writer, index=False)
    writer.save()
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
