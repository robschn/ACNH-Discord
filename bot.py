# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='turnip', help='Logs current price of turnips')
async def price(ctx, current_price: int):
    await ctx.send(f'Your current price of {current_price} has been logged!')

bot.run(TOKEN)