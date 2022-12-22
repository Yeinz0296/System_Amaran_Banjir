import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

'''
Data gather from the website and save to csv

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

# Web scrapping Algorithm
def web_scrapping(state, district):
    global state_url
    state_url = state
    global district_url
    district_url = district
    URL = "http://publicinfobanjir.water.gov.my/aras-air/data-paras-air/aras-air-data/?state={}&district={}&station=ALL".format(state_url, district_url)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find_all('tr', class_='item')

    # List to store 
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
    
    df = pd.DataFrame(param) 
    df.to_csv('data/JPS_{}_{}.csv'.format(state_url, district_url), index=False, encoding='utf-8')
    

def filter_status():
    df = pd.read_csv('data/JPS_{}_{}.csv'.format(state_url, district_url))

    conditions=[
        (df['Aras Air'] <= df['Normal']),
        (df['Aras Air'] >= df['Normal'])  & (df['Aras Air'] <= df['Waspada']),
        (df['Aras Air'] >= df['Waspada']) & (df['Aras Air'] <= df['Amaran']),
        (df['Aras Air'] >= df['Amaran'])  & (df['Aras Air'] <= df['Bahaya']),
        (df['Aras Air'] >= df['Bahaya'])
    ]

    choices=["Cetek","Normal","Waspada","Amaran","Bahaya"]
    df['Status'] = np.select(conditions, choices,default='Tiada Bacaan')
    return df

short = ['PLS','KDH','PNG','PRK','SEL','WLH','NSN','MLK','JHR','PHG','TRG','KEL','SRK','SAB','WLP']
if __name__ == '__main__':
    web_scrapping('WLP', 'ALL')
    filter_status()