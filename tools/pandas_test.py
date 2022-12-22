import pandas as pd
import numpy as np

df = pd.read_csv('data/JPS_KDH_ALL.csv', index_col=False)

conditions=[
    (df['Aras Air'] <= df['Normal']),
    (df['Aras Air'] >= df['Normal'])&(df['Aras Air'] <= df['Waspada']),
    (df['Aras Air'] >= df['Waspada'])&(df['Aras Air'] <= df['Amaran']),
    (df['Aras Air'] >= df['Amaran'])&(df['Aras Air'] <= df['Bahaya']),
    (df['Aras Air'] >= df['Bahaya']),
    ]
choices=["Cetek","Normal","Waspada","Amaran","Bahaya"]
df['Status'] = np.select(conditions, choices,default='Tiada Bacaan')

print(df)

status = ['Waspada','Amaran','Bahaya']

filter_data = df.loc[df['Status'].isin(status)]

print(filter_data)

if filter_data[filter_data['Status'].isin(['Cetek'])].bool:
    print(filter_data)

else:
    print("false")

print(df['Daerah'])

