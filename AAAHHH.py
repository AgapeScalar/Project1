import requests
res=requests.get('https://privatbank.ua/')
res_text=res.text
res_parse=res_text.split('<td>')
coin=[]
for elem in res_parse:
    if elem.startswith('$'):
        for el in elem.split('</td>'):
            if el.startswith('$') and el[1].isdigit():
                #print(el)
                coin.append(el)
bitcoin=coin[0]
print('cost Dollar =',bitcoin)
#
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
# url='https://privatbank.ua/'
# file='work.cvs'
# res=requests.get(url)
# if res.status_code==200:
#     soup=bs(res.text, features='html.parser')
#     soup_list=soup.find_all('h2',class_='')
#     for name in soup_list:
#         print(name.a['title'])
#     soup_list2=soup.find_all('b',class_='')
#     for num in soup_list2:
#         print(num.text)
# def ress(site=url):
#     inf={'title':[],'zarplata':[]}
#     res = requests.get(site)
#     soup=bs(res.text, features='html.parser')
#     soup_list=soup.find_all('h2',class_='')
#     for name in soup_list:
#         inf['title'].append(name.a['title'])
#     soup_list2=soup.find_all('b',class_='')
#     for num in soup_list2:
#         inf['zarplata'].append(num.text)
#     return inf
# dannie=['title','zarplata']
# f=pd.DataFrame(data=ress(),columns=dannie)
# f.to_csv(file,sep=';',charset='utf8')
#






















