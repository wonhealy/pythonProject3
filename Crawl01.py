import urllib.request
from bs4 import BeautifulSoup

try:

    url ='https://finance.naver.com/sise/sise_market_sum.naver'
    src_code= urllib.request.urlopen(url)
    #
    plain_text =src_code.read().decode('euc-kr')
    #
    convert_data = BeautifulSoup(plain_text,'html.parser')
    for start in[2,10,18,26,34,42,50,58,66,74]:
         for i in range(2,7):
            selector1 =f'#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child({i}) > td:nth-child(2) > a'
            stock=convert_data.select_one(selector1)
            name = stock.string
            print('종목명: ',name)#종목명
            print('종목코드: ',stock['href'][-6:],name,end='')# 종목코드,코드명
            selector1 =f'#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child({i}) > td:nth-child(3)'
            price=convert_data.select_one(selector1)
            price=price.string
            print(f'{price:9s}',end='') # 현재가
            selector1 = f'#contentarea > div.box_type_l > table.type_2 > thead > tr > th:nth-child({i})'
            amount= convert_data.select_one(selector1)
            amount= amount.string
            print(f'{amount:20s}') # 시가 총액



except Exception as e:
    print('Error : ',e)
