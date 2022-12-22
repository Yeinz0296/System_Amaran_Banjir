from banjir_bot.Perlis import *
from banjir_bot.Kedah import *
from banjir_bot.Penang import *
from banjir_bot.Perak import *
from banjir_bot.Selangor import *
from banjir_bot.WPKL import *
from banjir_bot.Negeri9 import *
from banjir_bot.Melaka import *
from banjir_bot.Johor import *
from banjir_bot.Pahang import *
from banjir_bot.Terengganu import *
from banjir_bot.Kelantan import *
from banjir_bot.Sarawak import *
from banjir_bot.Sabah import *
from banjir_bot.WPL import *

async def negeri_command(update, context):
    await update.message.reply_html('''Ini senarai negeri yang bot ini cover
1. /Perlis
2. /Kedah
3. /Pulau_Pinang
4. /Perak
5. /Selangor
6. /WP_Kuala_Lumpur
7. /Negeri_Sembilan	
8. /Melaka	
9. /Johor	
10. /Pahang	
11. /Terengganu	
12. /Kelantan	
13. /Sarawak	
14. /Sabah	
15. /WP_Labuan
''')