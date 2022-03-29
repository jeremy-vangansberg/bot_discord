import discord
from discord.ext import tasks 
import time
import os
import datetime

# local version
# from dotenv import load_dotenv
# load_dotenv()

# ID_SERVER = int(os.getenv('ID_SERVER'))
# ID_CHANNEL = int(os.getenv('ID_CHANNEL'))
# TOKEN =os.getenv('TOKEN')

# Heroku version
ID_SERVER = int(os.environ['ID_SERVER'])
ID_CHANNEL = int(os.environ['ID_CHANNEL'])
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    mytask.start()

@tasks.loop(seconds=60)#1 min
async def mytask():
    channel = client.get_guild(ID_SERVER).get_channel(ID_CHANNEL)
    strings = time.strftime("%H:%M")
    today = datetime.date.today().isoweekday()
    if today in [1,2,3,4,5] :
        if strings in ["08:00","90:00","12:30","14:00"] :
            await channel.send("Rappel : n'oubliez pas de signer sur SWS <@&913805722511355965>")       

client.run(TOKEN)
