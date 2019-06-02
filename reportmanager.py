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

def alpha2num(alpha):
    num=0
    for index, item in enumerate(list(alpha)):
        num += pow(26,len(alpha)-index-1)*(ord(item)-ord('A')+1)
    return num

def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)

cell = alpha2num("AA")

check_data = wks.acell( num2alpha(cell) + "14").value

while "http" in check_data:
    cell = cell + 1
    check_data = wks.acell( num2alpha(cell) + "14").value
else:
    wks.update_acell( num2alpha(cell) + "14", str(soup.item.link.string))

print(num2alpha(cell) + "14" + "is compleate.")
