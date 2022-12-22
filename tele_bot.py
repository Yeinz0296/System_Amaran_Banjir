import logging
from secret import secret
from telegram import *
from telegram.ext import *
from banjir_bot.negeri import * #To get list of the state & district

# To log the process
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logging.getLogger(__name__)
logging.info('Bot tengah run...')

async def start_command(update: Update, context: ContextTypes):
    user = update.effective_user
    print(user)
    await update.message.reply_html(f'Selamat datang {user.mention_html()}, saya @Amaran_banjir_bot, apa boleh saya bantu anda?')

async def help_command(update, context):
    await update.message.reply_text('Apa boleh saya bantu anda?')

async def status_command(update, context):
    await update.message.reply_text('Untuk masa ini, bot ini masih hidup')

def error(update, context):
    logging.error(f'Update {update} caused error {context.error}')

def main_tele_bot():
    app = ApplicationBuilder().token(secret['Telegram_API']).build()

    # Command
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('status', status_command))

    # banjir_bot.negeri
    app.add_handler(CommandHandler('negeri', negeri_command))

    #Perlis
    app.add_handler(CommandHandler('Perlis', Perlis_command))
    app.add_handler(CommandHandler('Padang_Besar', Padang_Besar_command))
    app.add_handler(CommandHandler('Arau', Arau_command))
    app.add_handler(CommandHandler('Kangar', Kangar_command))

    #Kedah
    app.add_handler(CommandHandler('Kedah', Kedah_command))
    app.add_handler(CommandHandler('Langkawi', Langkawi_command))
    app.add_handler(CommandHandler('Kubang_Pasu', Kubang_Pasu_command))
    app.add_handler(CommandHandler('Padang_Terap', Padang_Terap_command))
    app.add_handler(CommandHandler('Kota_Setar', Kota_Setar_command))
    app.add_handler(CommandHandler('Pendang', Pendang_command))
    app.add_handler(CommandHandler('Sik', Sik_command))
    app.add_handler(CommandHandler('Baling', Baling_command))
    app.add_handler(CommandHandler('Kuala_Muda', Kuala_Muda_command))
    app.add_handler(CommandHandler('Yan', Yan_command))
    app.add_handler(CommandHandler('Kulim', Kulim_command))
    app.add_handler(CommandHandler('Bandar_Baharu', Bandar_Baharu_command))

    #Penang
    app.add_handler(CommandHandler('Pulau_Pinang', Pulau_Pinang_command))
    app.add_handler(CommandHandler('Seberang_Perai_Utara', Seberang_Perai_Utara_command))
    app.add_handler(CommandHandler('Seberang_Perai_Tengah', Seberang_Perai_Tengah_command))
    app.add_handler(CommandHandler('Seberang_Perai_Selatan', Seberang_Perai_Selatan_command))
    app.add_handler(CommandHandler('Timur_Laut_Pulau_Pinang', Timur_Laut_Pulau_Pinang_command))
    app.add_handler(CommandHandler('Barat_Daya_Pulau_Pinang', Barat_Daya_Pulau_Pinang_command))

    #Perak
    app.add_handler(CommandHandler('Perak', Perak_command))
    app.add_handler(CommandHandler('Larut_Matang_dan_Selama', Larut_Matang_dan_Selama_command))
    app.add_handler(CommandHandler('Kerian', Kerian_command))
    app.add_handler(CommandHandler('Hulu_Perak', Hulu_Perak_command))
    app.add_handler(CommandHandler('Kuala_Kangsar', Kuala_Kangsar_command))
    app.add_handler(CommandHandler('Kinta', Kinta_command))
    app.add_handler(CommandHandler('Perak_Tengah', Perak_Tengah_command))
    app.add_handler(CommandHandler('Muallim', Muallim_command))
    app.add_handler(CommandHandler('Bagan_Datuk', Bagan_Datuk_command))

    #Selangor
    app.add_handler(CommandHandler('Selangor', Selangor_command))
    app.add_handler(CommandHandler('Hulu_Selangor', Hulu_Selangor_command))
    app.add_handler(CommandHandler('Sabak_Bernam', Sabak_Bernam_command))
    app.add_handler(CommandHandler('Kuala_Selangor', Kuala_Selangor_command))
    app.add_handler(CommandHandler('Gombak', Gombak_command))
    app.add_handler(CommandHandler('Petaling', Petaling_command))
    app.add_handler(CommandHandler('Klang', Klang_command))
    app.add_handler(CommandHandler('Hulu_Langat', Hulu_Langat_command))
    app.add_handler(CommandHandler('Sepang', Sepang_command))
    app.add_handler(CommandHandler('Kuala_Langat', Kuala_Langat_command))

    #WP_KL
    app.add_handler(CommandHandler('WP_Kuala_Lumpur', WP_Kuala_Lumpur_command))
    app.add_handler(CommandHandler('Gombak_WPKL', Gombak_WPKL_command))
    app.add_handler(CommandHandler('Kuala_Lumpur', Kuala_Lumpur_command))

    #Negeri_Sembilan
    app.add_handler(CommandHandler('Negeri_Sembilan', Negeri_Sembilan_command))
    app.add_handler(CommandHandler('Seremban', Seremban_command))
    app.add_handler(CommandHandler('Port_Dickson', Port_Dickson_command))
    app.add_handler(CommandHandler('Rembau', Rembau_command))
    app.add_handler(CommandHandler('Jelebu', Jelebu_command))
    app.add_handler(CommandHandler('Jempol', Jempol_command))
    app.add_handler(CommandHandler('Kuala_Pilah', Kuala_Pilah_command))
    app.add_handler(CommandHandler('Tampin', Tampin_command))

    #Melaka	
    app.add_handler(CommandHandler('Melaka', Melaka_command))
    app.add_handler(CommandHandler('Alor_Gajah', Alor_Gajah_command))
    app.add_handler(CommandHandler('Jasin', Jasin_command))
    app.add_handler(CommandHandler('Melaka_Tengah', Melaka_Tengah_command))
    
    #Johor
    app.add_handler(CommandHandler('Johor', Johor_command))
    app.add_handler(CommandHandler('Segamat', Segamat_command))
    app.add_handler(CommandHandler('Muar', Muar_command))
    app.add_handler(CommandHandler('Tangkak', Tangkak_command))
    app.add_handler(CommandHandler('Batu_Pahat', Batu_Pahat_command))
    app.add_handler(CommandHandler('Kluang', Kluang_command))
    app.add_handler(CommandHandler('Kulai', Kulai_command))
    app.add_handler(CommandHandler('Pontian', Pontian_command))
    app.add_handler(CommandHandler('Johor_Bahru', Johor_Bahru_command))
    app.add_handler(CommandHandler('Kota_Tinggi', Kota_Tinggi_command))
    app.add_handler(CommandHandler('Mersing', Mersing_command))

    #Pahang	
    app.add_handler(CommandHandler('Pahang', Pahang_command))
    app.add_handler(CommandHandler('Cameron_Highlands', Cameron_Highlands_command))
    app.add_handler(CommandHandler('Lipis', Lipis_command))
    app.add_handler(CommandHandler('Jerantut', Jerantut_command))
    app.add_handler(CommandHandler('Raub', Raub_command))
    app.add_handler(CommandHandler('Bentong', Bentong_command))
    app.add_handler(CommandHandler('Temerloh', Temerloh_command))
    app.add_handler(CommandHandler('Bera', Bera_command))
    app.add_handler(CommandHandler('Maran', Maran_command))
    app.add_handler(CommandHandler('Pekan', Pekan_command))
    app.add_handler(CommandHandler('Kuantan', Kuantan_command))
    app.add_handler(CommandHandler('Rompin', Rompin_command))

    #Terengganu	
    app.add_handler(CommandHandler('Terengganu', Terengganu_command))
    app.add_handler(CommandHandler('Besut', Besut_command))
    app.add_handler(CommandHandler('Setiu', Setiu_command))
    app.add_handler(CommandHandler('Hulu_Terengganu', Hulu_Terengganu_command))
    app.add_handler(CommandHandler('Kuala_Terengganu', Kuala_Terengganu_command))
    app.add_handler(CommandHandler('Kuala_Nerus', Kuala_Nerus_command))
    app.add_handler(CommandHandler('Marang', Marang_command))
    app.add_handler(CommandHandler('Dungun', Dungun_command))
    app.add_handler(CommandHandler('Kemaman', Kemaman_command))

    #Kelantan
    app.add_handler(CommandHandler('Kelantan', Kelantan_command))
    app.add_handler(CommandHandler('Gua_Musang', Gua_Musang_command))
    app.add_handler(CommandHandler('Kuala_Krai', Kuala_Krai_command))
    app.add_handler(CommandHandler('Jeli', Jeli_command))
    app.add_handler(CommandHandler('Tanah_Merah', Tanah_Merah_command))
    app.add_handler(CommandHandler('Pasir_Mas', Pasir_Mas_command))
    app.add_handler(CommandHandler('Kota_Bharu', Kota_Bharu_command))
    app.add_handler(CommandHandler('Tumpat', Tumpat_command))
    app.add_handler(CommandHandler('Bachok', Bachok_command))
    app.add_handler(CommandHandler('Pasir_Puteh', Pasir_Puteh_command))	

    #Sarawak	
    app.add_handler(CommandHandler('Sarawak', Sarawak_command))
    app.add_handler(CommandHandler('Kuching', Kuching_command))
    app.add_handler(CommandHandler('Serian', Serian_command))
    app.add_handler(CommandHandler('Samarahan', Samarahan_command))
    app.add_handler(CommandHandler('Sri_Aman', Sri_Aman_command))
    app.add_handler(CommandHandler('Betong', Betong_command))
    app.add_handler(CommandHandler('Kapit', Kapit_command))
    app.add_handler(CommandHandler('Sibu', Sibu_command))
    app.add_handler(CommandHandler('Sarikei', Sarikei_command))
    app.add_handler(CommandHandler('Mukah', Mukah_command))
    app.add_handler(CommandHandler('Bintulu', Bintulu_command))
    app.add_handler(CommandHandler('Miri', Miri_command))
    app.add_handler(CommandHandler('Limbang', Limbang_command))

    #Sabah	
    app.add_handler(CommandHandler('Sabah', Sabah_command))
    app.add_handler(CommandHandler('Tenom', Tenom_command))
    app.add_handler(CommandHandler('Tambunan', Tambunan_command))
    app.add_handler(CommandHandler('Keningau', Keningau_command))
    app.add_handler(CommandHandler('Kinabatangan', Kinabatangan_command))
    app.add_handler(CommandHandler('Penampang', Penampang_command))
    app.add_handler(CommandHandler('Kudat', Kudat_command))

    #WP_Labuan
    app.add_handler(CommandHandler('WP_Labuan', WP_Labuan_command))
    app.add_handler(CommandHandler('Labuan', Labuan_command))

    # Log error
    app.add_error_handler(error)

    # Run the bot
    app.run_polling()

if __name__ == '__main__':
    main_tele_bot()
