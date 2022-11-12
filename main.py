import requests
import secret #To store secret keys such as API
import json
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


'''
Location Zone - Change to better suit your location
'''
state_url ='SEL'
district_url ='ALL'

'''
List Zone
'''
Bilangan = []
id_station = []
name_station = []
Daerah = []
Lembangan = []
Sub_Lembangan = []
aras_air = []
Kemaskini_Terakhir = []
Normal = []
Waspada = []
Amaran = []
Bahaya = []

status = ['Waspada','Amaran','Bahaya']
'''
Function Zone
'''
def pushbullet_noti(title, body):
 
    TOKEN = secret.secret['Pushbullet_api']  # Pass your Access Token here
    # Make a dictionary that includes, title and body
    global msg
    msg = {"type": "note", "title": title, "body": str(body)}
    # Sent a posts request
    resp = requests.post('https://api.pushbullet.com/v2/pushes',
                         data=json.dumps(msg),
                         headers={'Authorization': 'Bearer ' + TOKEN,
                                  'Content-Type': 'application/json'})
    if resp.status_code != 200:  # Check if fort message send with the help of status code
        raise Exception('Error', resp.status_code)
    else:
        print('Message sent')

'''
Web scarping zone
'''
URL = "http://publicinfobanjir.water.gov.my/aras-air/data-paras-air/aras-air-data/?state={}&district={}&station=ALL".format(state_url, district_url)
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

'''
Data gather and save to csv

data-th="No"
data-th="Station ID"
data-th="Station Name"
data-th="District"
data-th="Main Basin (mm)"
data-th="Sub River Basin (mm)"
data-th="Last Update"
a
data-th="Normal"
data-th="Alert"
data-th="Warning"
data-th="Danger"
'''

results = soup.find_all('tr', class_='item')

for result in results:
    '''
    Get data from the row and column
    '''
    no = result.find('td', attrs={'data-th':"No"})
    id = result.find('td', attrs={'data-th':"Station ID"})
    nama = result.find('td', attrs={'data-th':"Station Name"})
    district = result.find('td', attrs={'data-th':"District"})
    basin = result.find('td', attrs={'data-th':"Main Basin (mm)"})
    sub_basin = result.find('td', attrs={'data-th':"Sub River Basin (mm)"})
    masa = result.find('td', attrs={'data-th':"Last Update"})
    level_now = result.find('a')
    normal = result.find('td', attrs={'data-th':"Normal"})
    alert = result.find('td', attrs={'data-th':"Alert"})
    warning = result.find('td', attrs={'data-th':"Warning"})
    danger = result.find('td', attrs={'data-th':"Danger"})
    
    '''
    Append the data into the list
    '''
    Bilangan.append(no.text)
    id_station.append(id.text)
    name_station.append(nama.text.strip())
    Daerah.append(district.text.strip())
    Lembangan.append(basin.text.strip())
    Sub_Lembangan.append(sub_basin.text.strip())
    Kemaskini_Terakhir.append(masa.text.strip())
    aras_air.append(level_now.text.strip())
    Normal.append(normal.text.strip())
    Waspada.append(alert.text.strip())
    Amaran.append(warning.text.strip())
    Bahaya.append(danger.text.strip())

param ={
    'Bilangan':Bilangan,
    'ID Stesen':id_station,
    'Nama Stesen':name_station,
    'Daerah':Daerah,
    'Lembangan':Lembangan,
    'Sub Lembangan':Sub_Lembangan,
    'Update sekarang':Kemaskini_Terakhir, 
    'Aras Air':aras_air,
    'Normal':Normal,
    'Waspada':Waspada,
    'Amaran':Amaran,
    'Bahaya':Bahaya
    }

'''
Save the data to csv using pandas
'''
df = pd.DataFrame(param) 
df.to_csv('data/JPS_{}_{}.csv'.format(state_url, district_url), index=False, encoding='utf-8')

'''
Open the csv file
'''
df = pd.read_csv('data/JPS_{}_{}.csv'.format(state_url, district_url))

conditions=[
    (df['Aras Air'] <= df['Normal']),
    (df['Aras Air'] >= df['Normal'])  & (df['Aras Air'] <= df['Waspada']),
    (df['Aras Air'] >= df['Waspada']) & (df['Aras Air'] <= df['Amaran']),
    (df['Aras Air'] >= df['Amaran'])  & (df['Aras Air'] <= df['Bahaya']),
    (df['Aras Air'] >= df['Bahaya'])]

choices=["Cetek","Normal","Waspada","Amaran","Bahaya"]
df['Status'] = np.select(conditions, choices,default='Tiada Bacaan')

for data in status:
    df_noti = df.loc[df['Status'].isin([data])]
    result = df_noti.to_json(orient='index')
    parsed = json.loads(result)

    for p_id, p_info in parsed.items():
        print("\nIndex ID:", p_id)
        data_to_push =f'''
ID Stesen: {parsed[p_id]['ID Stesen']}
Nama Stesen: {parsed[p_id]['Nama Stesen']}
Daerah: {parsed[p_id]['Daerah']}
Lembangan: {parsed[p_id]['Lembangan']}
Sub Lembangan: {parsed[p_id]['Sub Lembangan']}
Update sekarang: {parsed[p_id]['Update sekarang']}
Aras Air: {parsed[p_id]['Aras Air']}
Status: {parsed[p_id]['Status']}
'''
        pushbullet_noti("Amaran banjir", data_to_push)
