import time
import datetime
from discord import Webhook, RequestsWebhookAdapter
import pytz

# local version
# from dotenv import load_dotenv
# load_dotenv()

# DISCORD_WEBHOOK = os.environ['DISCORD_WEBHOOK']

# Heroku version

DISCORD_WEBHOOK = "https://discord.com/api/webhooks/993440182185504804/QUY7fkpaLFIMIfr6tVSzC8PuX5bdyfZOXA_xfZXtxfqr-LagxjoSlvSIHqp-axF8chBp"


def loop():
    paris = pytz.timezone('Europe/Paris')
    dt = datetime.datetime.now()
    dls = time.localtime().tm_isdst
    if dls:
        loc_dt1 = paris.localize(dt, is_dst=True)
    else:
        loc_dt1 = paris.localize(dt, is_dst=False)

    hour = str(loc_dt1.hour)
    minute = str(loc_dt1.minute)
    weekday = str(loc_dt1.weekday()+1)

    hour_to_test = "{}:{}".format(hour, minute)

    hours_to_push = ["10:00", "11:00", "15:00", "16:00"]

    if weekday in ['1', '2', '3', '4', '5']:
        if hour_to_test in hours_to_push:
            webhook = Webhook.from_url(
                DISCORD_WEBHOOK, adapter=RequestsWebhookAdapter())
            webhook.send(
                "Rappel : n'oubliez pas de signer sur SWS <@&913805722511355965>")


while True:
    loop()
    time.sleep(60)
