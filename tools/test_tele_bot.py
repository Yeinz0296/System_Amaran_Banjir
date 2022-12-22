import logging
from secret import secret
from telegram.ext import *
from banjir_bot.negeri import * #Untuk dapatkan list negeri

# To log the process
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logging.info('Bot tengah run...')

