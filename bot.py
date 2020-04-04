# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv
import pandas as pd
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='purchase_price', help='Logs purchase price of turnips')
async def purchase_price(ctx, purchase_price: int):
    await ctx.send(f'Your purchase price of {purchase_price} has been logged!')
    # todo insertPurhcase()
    # return purchase_price


@bot.command(name='current_price', help='Logs current price of turnips')
async def current_price(ctx, current_price: int):
    username = ctx.author
    await ctx.send(f'{username}! Your current price of {current_price} has been logged!')
    # return current_price

# @bot.command(name='stalk', help='Runs turnip price report')
# async def stalk(ctx):
#     return_purchase = purchase_price()
#     return_current = current_price()
#     await ctx.send(
#     f'You purchased turnips at {return_purchase} bells\nHere is the current price: {return_current}'
#     )

# Context.guild to fetch the Guild of the command, if any.

# Context.message to fetch the Message of the command.

# Context.author to fetch the Member or User that called the command.

# Context.send() to send a message to the channel the command was used in.

bot.run(TOKEN)


# def createSpread(filename):
#     data = pd.DataFrame()
#     data[['Purchase Price', 'Sell Price', 'Time', 'Author Name']] = [0], [0], [pd.datetime.now()], ['admin']
#     data.to_csv('./Data/data.csv')

# def insertPurhcase(purchase_price, author):
    #todo code to load csv, append row, save and close csv
