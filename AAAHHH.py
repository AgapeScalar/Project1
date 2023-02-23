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



















