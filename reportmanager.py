import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup
import requests

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('reportmanager-a6d8efaf502e.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key('1IeIOQtXMMy-Lhv36F2KRTGqjSJsAKbutuZ6aRrlk_yo').get_worksheet(3)

url = 'https://medium.com/feed/@koukitakesue'
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
req = requests.get(url=url, headers=headers)

soup = BeautifulSoup(req.content, "xml")

wks.update_acell('F14', str(soup.item.link.string))
print(wks.acell('F14'))
