import urllib.request
from bs4 import BeautifulSoup

try:
    url ='https://finance.naver.com/sise/sise_market_sum.naver'
    src_code= urllib.request.urlopen(url)

    plain_text =src_code.read().decode('euc-kr')

    convert_data = BeautifulSoup(plain_text,'html.parser')

    for atag in convert_data.findAll('a'):
        print(atag.string)
except Exception as e:
    print('Error: ',e)
