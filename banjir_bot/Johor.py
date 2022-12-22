from data_jps import *
import json

async def Johor_command(update, context):
    await update.message.reply_text('''Ini senarai daerah dalam /Johor
1. /Segamat
2. /Muar
3. /Tangkak
4. /Batu_Pahat
5. /Kluang
6. /Kulai
7. /Pontian
8. /Johor_Bahru
9. /Kota_Tinggi
10. /Mersing
''')

async def Segamat_command(update, context):
    web_scrapping('JHR', 'Segamat')
    status = ["Cetek","Normal","Waspada","Amaran","Bahaya"]
    for data in status:
        df_noti = filter_status().loc[filter_status()['Status'].isin([data])]
        result = df_noti.to_json(orient='index')
        parsed = json.loads(result)
        for p_id, p_info in parsed.items():
            print("Index ID:", p_id)
            data_to_push =f'''
ID Stesen: {parsed[p_id]['ID Stesen']}
Nama Stesen: {parsed[p_id]['Nama Stesen']}
Daerah: {parsed[p_id]['Daerah']}
Lembangan: {parsed[p_id]['Lembangan']}
Sub Lembangan: {parsed[p_id]['Sub Lembangan']}
Update sekarang: {parsed[p_id]['Update sekarang']}
Aras Air: {parsed[p_id]['Aras Air']}
Status: {parsed[p_id]['Status']}'''
            await update.message.reply_text(data_to_push)


async def Muar_command(update, context):
    web_scrapping('JHR', 'Muar')
    status = ["Cetek","Normal","Waspada","Amaran","Bahaya"]
    for data in status:
        df_noti = filter_status().loc[filter_status()['Status'].isin([data])]
        result = df_noti.to_json(orient='index')
        parsed = json.loads(result)
        for p_id, p_info in parsed.items():
            print("Index ID:", p_id)
            data_to_push =f'''
ID Stesen: {parsed[p_id]['ID Stesen']}
Nama Stesen: {parsed[p_id]['Nama Stesen']}
Daerah: {parsed[p_id]['Daerah']}
Lembangan: {parsed[p_id]['Lembangan']}
Sub Lembangan: {parsed[p_id]['Sub Lembangan']}
Update sekarang: {parsed[p_id]['Update sekarang']}
Aras Air: {parsed[p_id]['Aras Air']}
Status: {parsed[p_id]['Status']}'''
            await update.message.reply_text(data_to_push)


async def Tangkak_command(update, context):
    web_scrapping('JHR', 'Tangkak')
    status = ["Cetek","Normal","Waspada","Amaran","Bahaya"]
    for data in status:
        df_noti = filter_status().loc[filter_status()['Status'].isin([data])]
        result = df_noti.to_json(orient='index')
        parsed = json.loads(result)
        for p_id, p_info in parsed.items():
            print("Index ID:", p_id)
            data_to_push =f'''
ID Stesen: {parsed[p_id]['ID Stesen']}
Nama Stesen: {parsed[p_id]['Nama Stesen']}
Daerah: {parsed[p_id]['Daerah']}
Lembangan: {parsed[p_id]['Lembangan']}
Sub Lembangan: {parsed[p_id]['Sub Lembangan']}
Update sekarang: {parsed[p_id]['Update sekarang']}
Aras Air: {parsed[p_id]['Aras Air']}
Status: {parsed[p_id]['Status']}'''
            await update.message.reply_text(data_to_push)


async def Batu_Pahat_command(update, context):
    web_scrapping('JHR', 'Batu Pahat')
    status = ["Cetek","Normal","Waspada","Amaran","Bahaya"]
    for data in status:
        df_noti = filter_status().loc[filter_status()['Status'].isin([data])]
        result = df_noti.to_json(orient='index')
        parsed = json.loads(result)
        for p_id, p_info in parsed.items():
            print("Index ID:", p_id)
            data_to_push =f'''
ID Stesen: {parsed[p_id]['ID Stesen']}
Nama Stesen: {parsed[p_id]['Nama Stesen']}
Daerah: {parsed[p_id]['Daerah']}
Lembangan: {parsed[p_id]['Lembangan']}
Sub Lembangan: {parsed[p_id]['Sub Lembangan']}
Update sekarang: {parsed[p_id]['Update sekarang']}
Aras Air: {parsed[p_id]['Aras Air']}
Status: {parsed[p_id]['Status']}'''
            await update.message.reply_text(data_to_push)


async def Kluang_command(update, context):
    web_scrapping('JHR', 'Kluang')
    status = ["Cetek","Normal","Waspada","Amaran","Bahaya"]
    for data in status:
        df_noti = filter_status().loc[filter_status()['Status'].isin([data])]
        result = df_noti.to_json(orient='index')
        parsed = json.loads(result)
        for p_id, p_info in parsed.items():
            print("Index ID:", p_id)
            data_to_push =f'''
ID Stesen: {parsed[p_id]['ID Stesen']}
Nama Stesen: {parsed[p_id]['Nama Stesen']}
Daerah: {parsed[p_id]['Daerah']}
Lembangan: {parsed[p_id]['Lembangan']}
Sub Lembangan: {parsed[p_id]['Sub Lembangan']}
Update sekarang: {parsed[p_id]['Update sekarang']}
Aras Air: {parsed[p_id]['Aras Air']}
Status: {parsed[p_id]['Status']}'''
            await update.message.reply_text(data_to_push)


async def Kulai_command(update, context):
    web_scrapping('JHR', 'Kulai')
    status = ["Cetek","Normal","Waspada","Amaran","Bahaya"]
    for data in status:
        df_noti = filter_status().loc[filter_status()['Status'].isin([data])]
        result = df_noti.to_json(orient='index')
        parsed = json.loads(result)
        for p_id, p_info in parsed.items():
            print("Index ID:", p_id)
            data_to_push =f'''
ID Stesen: {parsed[p_id]['ID Stesen']}
Nama Stesen: {parsed[p_id]['Nama Stesen']}
Daerah: {parsed[p_id]['Daerah']}
Lembangan: {parsed[p_id]['Lembangan']}
Sub Lembangan: {parsed[p_id]['Sub Lembangan']}
Update sekarang: {parsed[p_id]['Update sekarang']}
Aras Air: {parsed[p_id]['Aras Air']}
Status: {parsed[p_id]['Status']}'''
            await update.message.reply_text(data_to_push)


async def Pontian_command(update, context):
    web_scrapping('JHR', 'Pontian')
    status = ["Cetek","Normal","Waspada","Amaran","Bahaya"]
    for data in status:
        df_noti = filter_status().loc[filter_status()['Status'].isin([data])]
        result = df_noti.to_json(orient='index')
        parsed = json.loads(result)
        for p_id, p_info in parsed.items():
            print("Index ID:", p_id)
            data_to_push =f'''
ID Stesen: {parsed[p_id]['ID Stesen']}
Nama Stesen: {parsed[p_id]['Nama Stesen']}
Daerah: {parsed[p_id]['Daerah']}
Lembangan: {parsed[p_id]['Lembangan']}
Sub Lembangan: {parsed[p_id]['Sub Lembangan']}
Update sekarang: {parsed[p_id]['Update sekarang']}
Aras Air: {parsed[p_id]['Aras Air']}
Status: {parsed[p_id]['Status']}'''
            await update.message.reply_text(data_to_push)


async def Johor_Bahru_command(update, context):
    web_scrapping('JHR', 'Johor Bahru')
    status = ["Cetek","Normal","Waspada","Amaran","Bahaya"]
    for data in status:
        df_noti = filter_status().loc[filter_status()['Status'].isin([data])]
        result = df_noti.to_json(orient='index')
        parsed = json.loads(result)
        for p_id, p_info in parsed.items():
            print("Index ID:", p_id)
            data_to_push =f'''
ID Stesen: {parsed[p_id]['ID Stesen']}
Nama Stesen: {parsed[p_id]['Nama Stesen']}
Daerah: {parsed[p_id]['Daerah']}
Lembangan: {parsed[p_id]['Lembangan']}
Sub Lembangan: {parsed[p_id]['Sub Lembangan']}
Update sekarang: {parsed[p_id]['Update sekarang']}
Aras Air: {parsed[p_id]['Aras Air']}
Status: {parsed[p_id]['Status']}'''
            await update.message.reply_text(data_to_push)


async def Kota_Tinggi_command(update, context):
    web_scrapping('JHR', 'Kota Tinggi')
    status = ["Cetek","Normal","Waspada","Amaran","Bahaya"]
    for data in status:
        df_noti = filter_status().loc[filter_status()['Status'].isin([data])]
        result = df_noti.to_json(orient='index')
        parsed = json.loads(result)
        for p_id, p_info in parsed.items():
            print("Index ID:", p_id)
            data_to_push =f'''
ID Stesen: {parsed[p_id]['ID Stesen']}
Nama Stesen: {parsed[p_id]['Nama Stesen']}
Daerah: {parsed[p_id]['Daerah']}
Lembangan: {parsed[p_id]['Lembangan']}
Sub Lembangan: {parsed[p_id]['Sub Lembangan']}
Update sekarang: {parsed[p_id]['Update sekarang']}
Aras Air: {parsed[p_id]['Aras Air']}
Status: {parsed[p_id]['Status']}'''
            await update.message.reply_text(data_to_push)


async def Mersing_command(update, context):
    web_scrapping('JHR', 'Mersing')
    status = ["Cetek","Normal","Waspada","Amaran","Bahaya"]
    for data in status:
        df_noti = filter_status().loc[filter_status()['Status'].isin([data])]
        result = df_noti.to_json(orient='index')
        parsed = json.loads(result)
        for p_id, p_info in parsed.items():
            print("Index ID:", p_id)
            data_to_push =f'''
ID Stesen: {parsed[p_id]['ID Stesen']}
Nama Stesen: {parsed[p_id]['Nama Stesen']}
Daerah: {parsed[p_id]['Daerah']}
Lembangan: {parsed[p_id]['Lembangan']}
Sub Lembangan: {parsed[p_id]['Sub Lembangan']}
Update sekarang: {parsed[p_id]['Update sekarang']}
Aras Air: {parsed[p_id]['Aras Air']}
Status: {parsed[p_id]['Status']}'''
            await update.message.reply_text(data_to_push)

