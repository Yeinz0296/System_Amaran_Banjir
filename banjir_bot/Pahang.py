from data_jps import *
import json

async def Pahang_command(update, context):
    await update.message.reply_text('''Ini senarai daerah dalam /Pahang
1. /Cameron_Highlands
2. /Lipis
3. /Jerantut
4. /Raub
5. /Bentong
6. /Temerloh
7. /Bera
8. /Maran
9. /Pekan
10. /Kuantan
11. /Rompin
''')

async def Cameron_Highlands_command(update, context):
    web_scrapping('PHG', 'Cameron Highlands')
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


async def Lipis_command(update, context):
    web_scrapping('PHG', 'Lipis')
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


async def Jerantut_command(update, context):
    web_scrapping('PHG', 'Jerantut')
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


async def Raub_command(update, context):
    web_scrapping('PHG', 'Raub')
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


async def Bentong_command(update, context):
    web_scrapping('PHG', 'Bentong')
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


async def Temerloh_command(update, context):
    web_scrapping('PHG', 'Temerloh')
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


async def Bera_command(update, context):
    web_scrapping('PHG', 'Bera')
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


async def Maran_command(update, context):
    web_scrapping('PHG', 'Maran')
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


async def Pekan_command(update, context):
    web_scrapping('PHG', 'Pekan')
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


async def Kuantan_command(update, context):
    web_scrapping('PHG', 'Kuantan')
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


async def Rompin_command(update, context):
    web_scrapping('PHG', 'Rompin')
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