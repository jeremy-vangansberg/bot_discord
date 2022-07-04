import time
import os
import datetime
# import requests
from discord import Webhook, RequestsWebhookAdapter, Embed

# local version
# from dotenv import load_dotenv
# load_dotenv()

# DISCORD_WEBHOOK = os.environ['DISCORD_WEBHOOK']

# Heroku version

DISCORD_WEBHOOK = os.environ['DISCORD_WEBHOOK']

def loop():
    strings = time.strftime("%H:%M")
    today = datetime.date.today().isoweekday()
    if today in [1,2,3,4,5] :
        if strings in ["08:00","90:00","12:30","14:00"] :
            await channel.send("Rappel : n'oubliez pas de signer sur SWS <@&913805722511355965>")       

