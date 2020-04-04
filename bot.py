# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='purchased_price', help='Logs purchase price of turnips')
async def price(ctx, purchased_price: int):
    await ctx.send(f'Your purchase price of {purchased_price} has been logged!')
    return purchased_price

@bot.command(name='current_price', help='Logs current price of turnips')
async def price(ctx, current_price: int):
    await ctx.send(f'Your current price of {current_price} has been logged!')
    return current_price

@bot.command(name='stalk', help='Runs turnip price report')
async def price(ctx):
    purchase_price = purchase_price()
    current_price = current_price()
    await ctx.send(
    f'You purchased turnips at {purchase_price} bells',
    f'Here is the current price: {current_price}'
    )

bot.run(TOKEN)