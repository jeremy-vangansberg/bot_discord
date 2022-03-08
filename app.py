import discord
from discord.ext import tasks 
import time
import os

# from dotenv import load_dotenv
# load_dotenv()

ID_SERVER = int(os.getenv('ID_SERVER'))
ID_CHANNEL = int(os.getenv('ID_CHANNEL'))
TOKEN =os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    mytask.start()

@tasks.loop(seconds=60)#1 min
async def mytask():
    channel = client.get_guild(ID_SERVER).get_channel(ID_CHANNEL)
    strings = time.strftime("%H,%M")
    if strings in ["10,21","11,00","14,30","16,00","17:02"]:
        await channel.send("Rappel : n'oubliez pas de signer sur SWS <@&913805722511355965>")
        
client.run(TOKEN)