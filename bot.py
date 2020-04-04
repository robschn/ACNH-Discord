# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='purchase_price', help='Logs purchase price of turnips')
async def purchase_price(ctx, purchase_price: int):
    await ctx.send(f'Your purchase price of {purchase_price} has been logged!')
    # return purchase_price

@bot.command(name='current_price', help='Logs current price of turnips')
async def current_price(ctx, current_price: int):
    await ctx.send(f'Your current price of {current_price} has been logged!')
    # return current_price

# @bot.command(name='stalk', help='Runs turnip price report')
# async def stalk(ctx):
#     return_purchase = purchase_price()
#     return_current = current_price()
#     await ctx.send(
#     f'You purchased turnips at {return_purchase} bells\nHere is the current price: {return_current}'
#     )

bot.run(TOKEN)