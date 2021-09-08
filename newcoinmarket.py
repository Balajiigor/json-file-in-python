from os import name, remove
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv
import pandas as pd
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'500',
  'convert':'INR'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '02c65827-46a1-4766-86fc-c9833d6a3462',
}

session = Session()
session.headers.update(headers)
with open("sbitcoin.csv","w") as csvfile: 
  csvwriter = csv.writer(csvfile)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    fieldname = list(data["data"][0].keys())
    csvwriter.writerow(fieldname)
    for value in data["data"]:
      try:
        csvwriter.writerow(value.values())
      except:
        pass
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
df = pd.read_csv("sbitcoin.csv")
df.drop(columns=['quote'], axis=0, inplace=True)
df.to_csv("sbitcoin.csv")

with open("sbitcoin.csv", "r") as source:
    reader = csv.reader(source)
    with open("output.csv", "w") as result:
        writer = csv.writer(result)
        for r in reader:
          writer.writerow((r[1],r[2],r[5],r[6],r[8],r[9],r[10],r[13]))
