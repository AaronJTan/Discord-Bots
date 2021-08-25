import os
import requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='random', help='Sends a random dog image')
async def dog(ctx):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    dog_img = response.json()['message']
    await ctx.send(dog_img)
    
@bot.command(name='woof', help='Responds with "woof woof"')
async def woof(ctx):
    await ctx.send('https://tenor.com/bwH2L.gif')
    await ctx.send('🐩🐕 WOOF WOOF 🦮🐕‍🦺 ')
    
@bot.command(name='yorkie', help='Sends a random yorkie image')
async def yorkie(ctx):
    response = requests.get('https://dog.ceo/api/breed/terrier/yorkshire/images/random')
    dog_img = response.json()['message']
    await ctx.send(dog_img)
    
@bot.command(name='list_breeds', help='Returns list of breeds to use with `!breed [BREED_NAME]` command')
async def list_breeds(ctx):
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    dog_img = [*response.json()['message']]
    await ctx.send(dog_img)   
    
@bot.command(name='breed', help='Sends a random dog image from the inputted breed; `!breed [BREED_NAME]`')
async def breed(ctx, *, breed):
    response = requests.get('https://dog.ceo/api/breed/{breed}/images/random'.format(breed = breed))
    dog_img = response.json()['message']
    await ctx.send(dog_img)    
    
@breed.error
async def breed_error(ctx, error):
    await ctx.send("MISSING ARGUEMENT. Proper use: `!breed [BREED_NAME]`\nFor a list of breed names type `!list_breeds`")


bot.run(TOKEN)


