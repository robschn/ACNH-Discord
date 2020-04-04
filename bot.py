# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

bot = commands.Bot(command_prefix='!')

@bot.command(name='turnip', help='Logs current price of turnips')
async def price(ctx, current_price: int):
    await ctx.send(f'Your current price of {current_price} has been logged!')


bot.run(TOKEN)