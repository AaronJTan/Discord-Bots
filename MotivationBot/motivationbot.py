import os
import requests
import json
import time

from discord.ext import tasks, commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='quote', help='Sends a motivational quote')
async def random_quote(ctx):
    response = requests.get('https://zenquotes.io/api/random')
    data = json.loads(response.text)
    quote = data[0]['q'] + " – " + data[0]['a']
    await ctx.send(quote)

bot.run(TOKEN)


