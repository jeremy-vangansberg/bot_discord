import time
import os
import datetime
import requests
from discord import Webhook, RequestsWebhookAdapter, Embed

# local version
# from dotenv import load_dotenv
# load_dotenv()

# DISCORD_WEBHOOK = os.environ['DISCORD_WEBHOOK']

# Heroku version

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/993440182185504804/QUY7fkpaLFIMIfr6tVSzC8PuX5bdyfZOXA_xfZXtxfqr-LagxjoSlvSIHqp-axF8chBp"

def loop():
    strings = time.strftime("%H:%M")
    today = datetime.date.today().isoweekday()
    if today in [1,2,3,4,5] :
        if strings in ["09:00","11:11", "9:57", "11:59","10:00"] :
            webhook = Webhook.from_url(DISCORD_WEBHOOK, adapter=RequestsWebhookAdapter())
            webhook.send("[test-bot-dockerized]Rappel : n'oubliez pas de signer sur SWS <@&913805722511355965>")      

print(time.strftime("%H:%M"))

while True : 
    loop()
    time.sleep(60)

