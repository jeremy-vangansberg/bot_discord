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
    dls = time.localtime().tm_isdst
    hours_summer = ["08:00", "09:00", "13:00", "14:00"]
    hours_winter = ["09:00", "10:00", "14:00", "15:00"]
    if today in [1, 2, 3, 4, 5]:
        # Vérification si heure d'été ou heure d'hiver
        if dls:
            hours = hours_summer
        else:
            hours = hours_winter

        if strings in hours:
            webhook = Webhook.from_url(
                DISCORD_WEBHOOK, adapter=RequestsWebhookAdapter())
            webhook.send(
                "Rappel : n'oubliez pas de signer sur SWS <@&913805722511355965>")


while True:
    loop()
    time.sleep(60)
