# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv
import pandas as pd
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

def insertPurchase(purchase_price, author):

    data = pd.read_csv('data.csv')
    insert = pd.DataFrame(data =  {'Purchase Price':[purchase_price],
                                    'Sell Price':[0],
                                    'Time':[pd.datetime.now()],
                                    'Author Name':[author]})
    
    print(f'Saving : Purchase Price {purchase_price}, Time: {pd.datetime.now()}, Author: {author}')
    data.append(insert, ignore_index = True)
    data.to_csv('data.csv')
    print('Finished!')

@bot.command(name='purchase_price', help='Logs purchase price of turnips')
async def purchase_price(ctx, purchase_price: int):
    username = ctx.author
    insertPurchase(purchase_price, username)
    await ctx.send(f'@{username}! Your purchase price of {purchase_price} has been logged!')

    # return purchase_price


@bot.command(name='current_price', help='Logs current price of turnips')
async def current_price(ctx, current_price: int):
    username = ctx.author
    await ctx.send(f'@{username}! Your current price of {current_price} has been logged!')
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


# import pandas as pd

# data = pd.DataFrame(data =  {'Purchase Price':[0],
#                                        'Sell Price':[0],
#                                        'Time':[pd.datetime.now()],
#                                        'Author Name':['admin']})

# data.to_csv('data.csv')
