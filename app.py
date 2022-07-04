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
        if strings in ["09:00","09:14","10:00","13:30","15:00"] :
            webhook = Webhook.from_url(DISCORD_WEBHOOK, adapter=RequestsWebhookAdapter())
            webhook.send(content="Rappel : n'oubliez pas de signer sur SWS <@&913805722511355965>")

loop() 

