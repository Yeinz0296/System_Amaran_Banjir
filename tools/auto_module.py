def openfile(path):
    myfile = open(path, 'r')
    tempdata = myfile.read()
    datalist = tempdata.split('\n')
    datalist.pop()
    myfile.close()
    return datalist

Nama_negeri = 'WP Labuan'
Short_form = 'WLP'
no = 0

ID_Stesen ='{parsed[p_id][\'ID Stesen\']}'
Nama_Stesen='{parsed[p_id][\'Nama Stesen\']}'
Daerah='{parsed[p_id][\'Daerah\']}'
Lembangan='{parsed[p_id][\'Lembangan\']}'
Sub_Lembangan='{parsed[p_id][\'Sub Lembangan\']}'
Update_sekarang='{parsed[p_id][\'Update sekarang\']}'
Aras_Air='{parsed[p_id][\'Aras Air\']}'
Status='{parsed[p_id][\'Status\']}'

print('''
from data_jps import *
import json''')

print(f'''
async def {Nama_negeri.replace(" ", "_")}_command(update, context):
    await update.message.reply_text('\'\'Ini senarai daerah dalam /{Nama_negeri.replace(" ", "_")} ''')
for data in openfile('daerah.txt'):
    no = no + 1
    print(f'''{no}. /{data.replace(" ","_")}''')
print("""''')""")

for data in openfile('daerah.txt'):
    # print(f"""async def {data.replace(" ","_")}_command(update, context):""")
    print(f"""
async def {data.replace(" ","_")}_command(update, context):
    web_scrapping('{Short_form}', '{data}')
    status = ["Cetek","Normal","Waspada","Amaran","Bahaya"]
    for data in status:
        df_noti = filter_status().loc[filter_status()['Status'].isin([data])]
        result = df_noti.to_json(orient='index')
        parsed = json.loads(result)
        for p_id, p_info in parsed.items():
            print("Index ID:", p_id)
            data_to_push =f'''
ID Stesen: {ID_Stesen}
Nama Stesen: {Nama_Stesen}
Daerah: {Daerah}
Lembangan: {Lembangan}
Sub Lembangan: {Sub_Lembangan}
Update sekarang: {Update_sekarang}
Aras Air: {Aras_Air}
Status: {Status}'''
            await update.message.reply_text(data_to_push)
""")

print(f'''app.add_handler(CommandHandler('{Nama_negeri.replace(" ","_")}', {Nama_negeri.replace(" ","_")}_command))''')
for data in openfile('daerah.txt'):
    print(f'''app.add_handler(CommandHandler('{data.replace(" ","_")}', {data.replace(" ","_")}_command))''')  