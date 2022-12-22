from data_jps import *
import json

async def Kedah_command(update, context):
    await update.message.reply_text('''Ini senarai daerah dalam /Kedah
1. /Langkawi
2. /Kubang_Pasu
3. /Padang_Terap
4. /Kota_Setar
5. /Pendang
6. /Sik
7. /Baling
8. /Kuala_Muda
9. /Yan
10. /Kulim
11. /Bandar_Baharu
''')

async def Langkawi_command(update, context):
    web_scrapping('KDH', 'Langkawi')
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


async def Kubang_Pasu_command(update, context):
    web_scrapping('KDH', 'Kubang Pasu')
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


async def Padang_Terap_command(update, context):
    web_scrapping('KDH', 'Padang Terap')
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


async def Kota_Setar_command(update, context):
    web_scrapping('KDH', 'Kota Setar')
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


async def Pendang_command(update, context):
    web_scrapping('KDH', 'Pendang')
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


async def Sik_command(update, context):
    web_scrapping('KDH', 'Sik')
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


async def Baling_command(update, context):
    web_scrapping('KDH', 'Baling')
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


async def Kuala_Muda_command(update, context):
    web_scrapping('KDH', 'Kuala Muda')
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


async def Yan_command(update, context):
    web_scrapping('KDH', 'Yan')
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


async def Kulim_command(update, context):
    web_scrapping('KDH', 'Kulim')
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


async def Bandar_Baharu_command(update, context):
    web_scrapping('KDH', 'Bandar Baharu')
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