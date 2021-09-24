import urllib.request
from bs4 import BeautifulSoup
import pandas as pd


adress=[]
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016960")#漢口路(山西路~中清路間)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V440470")#德芳南路
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V028800")#經貿路
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V115901")#市政路-環中路橋外慢車道(往北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V003401")#臺灣大道-黎明路(往北)

adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V017100")#中清路一段/進化北路口(往北近端號誌桿)(往北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V017140")#中清路一段/進化北路口(往南近端號誌桿)(往南)

adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016940")#中清路一段(武昌路~漢口路間)(向南)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016700")#中清路二段(大連路~文心路間)(向北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V015140")#中清路二段(文心路~大連路間)(向南)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V003340")#中清路二段(經貿一路~大鵬路間)(向南)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V496200")#中清路二段(大鵬路~經貿一路間)(向北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V040600")#中清路二段(經貿一路~敦化路間)(向北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016100")#中清路二段、經貿七路(向北)
'''
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V018400")#中清路二段(經貿七路~經貿五路間)(向南)
'''
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016140")#中清路二段、經貿七路(向南)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V094800")#中清路二段、黎明路三段(向北)
adress.append("http://e-traffic.taichung.gov.tw/ATIS_TCC/Device/Showvd?id=V016040")#中清路二段、經貿九路(向南)


value=[]
#寫成i個陣列儲存
for i in range(len(adress)):
    data=[]
    html = urllib.request.urlopen(adress[i]).read()
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup)

#下載關鍵字
    table = soup.find('table', {'class': 'table table-bordered table-striped table-hover table-condensed'})
    trs = table.find_all('tr')[1:]
    rows = list()

#用逗號分隔
    for tr in trs:
        rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr('td')])
    print(rows)

#判斷網址有幾筆車流，取該車流出來
    for i in range(len(rows)):
        data.append(rows[i][2])
    print('volume:',data)

#加總車流量
    sum=0
    for j in range(len(data)):
        sum = int(data[j])+sum
    print(sum)

#將車流量存成陣列
    value.append(sum)
    #print('全部車流量:', value)

#抓取陣列
a=value[6]
print('中清路一段/進化北路口(往北近端號誌桿)(往南):', a)
b=value[7]
print('中清路一段(武昌路~漢口路間)(向南):', b)
c=value[9]
print('中清路二段(文心路~大連路間)(向南):', c)
d=value[10]
print('中清路二段(經貿一路~大鵬路間)(向南):', d)
e=value[14]
print('中清路二段、經貿七路(向南):', e)
f=value[16]
print("中清路二段、經貿九路(向南):", f)

   
    


#錯誤示範    
"""
    for i in range(len(rows)):
        if len(rows[i])<=1:
            data.append(rows[i][2])
        elif len(rows[i])>=2:
            data.append(rows[i][2])
    print(data)
"""