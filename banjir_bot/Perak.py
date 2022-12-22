from data_jps import *
import json


async def Perak_command(update, context):
    await update.message.reply_text('''Ini senarai daerah dalam /Perak
1. /Larut_Matang_dan_Selama
2. /Kerian
3. /Hulu_Perak
4. /Kuala_Kangsar
5. /Kinta
6. /Perak_Tengah
7. /Muallim
8. /Bagan_Datuk
''')

async def Larut_Matang_dan_Selama_command(update, context):
    web_scrapping('PRK', 'Larut Matang dan Selama')
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


async def Kerian_command(update, context):
    web_scrapping('PRK', 'Kerian')
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


async def Hulu_Perak_command(update, context):
    web_scrapping('PRK', 'Hulu Perak')
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


async def Kuala_Kangsar_command(update, context):
    web_scrapping('PRK', 'Kuala Kangsar')
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


async def Kinta_command(update, context):
    web_scrapping('PRK', 'Kinta')
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


async def Perak_Tengah_command(update, context):
    web_scrapping('PRK', 'Perak Tengah')
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


async def Muallim_command(update, context):
    web_scrapping('PRK', 'Muallim')
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


async def Bagan_Datuk_command(update, context):
    web_scrapping('PRK', 'Bagan Datuk')
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

