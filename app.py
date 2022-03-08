import discord
from discord.ext import tasks 
import time
import os

# from dotenv import load_dotenv
# load_dotenv()

# ID_SERVER = int(os.getenv('ID_SERVER'))
# ID_CHANNEL = int(os.getenv('ID_CHANNEL'))
# TOKEN =os.getenv('TOKEN')

ID_SERVER = int(os.environ['ID_SERVER'])
ID_CHANNEL = int(os.environ['ID_CHANNEL'])
TOKEN = os.environ['TOKEN']

print(type(ID_SERVER), type(ID_CHANNEL), type(TOKEN))

client = discord.Client()

@client.event
async def on_ready():
    print(type(ID_SERVER), type(ID_CHANNEL), type(TOKEN))
    mytask.start()

@tasks.loop(seconds=60)#1 min
async def mytask():
    print(type(ID_SERVER), type(ID_CHANNEL), type(TOKEN))
    channel = client.get_guild(ID_SERVER).get_channel(ID_CHANNEL)
    strings = time.strftime("%H,%M")
    if strings in ["10,43","11,00","14,30","16,00","17:02"]:
        await channel.send("Rappel : n'oubliez pas de signer sur SWS <@&913805722511355965>")
        
client.run(TOKEN)