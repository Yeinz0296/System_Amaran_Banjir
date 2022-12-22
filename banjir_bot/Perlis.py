import json
from data_jps import web_scrapping, filter_status

async def Perlis_command(update, context):
    await update.message.reply_text('''Ini senarai daerah dalam /Perlis
1. /Arau
2. /Kangar
3. /Padang_Besar
''')

async def send_data(update, district):
    web_scrapping('PLS', district)
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

async def Arau_command(update, context):
    await send_data(update, 'Arau')

async def Kangar_command(update, context):
    await send_data(update, 'Kangar')

async def Padang_Besar_command(update, context):
    await send_data(update, 'Padang Besar')
