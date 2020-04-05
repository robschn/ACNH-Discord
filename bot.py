#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:00:00 2020
@author: Robert Schneider
"""
import os
import time

import pandas as pd
from discord.ext import commands
from dotenv import load_dotenv

import botfunctions


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='purchase_price', help='Logs purchase price of turnips')
async def purchase_price(ctx, purchase_price: int):
    username = ctx.author.strip('#')
    botfunctions.insertPurchase(purchase_price, username)
    await ctx.send(f'@{username} Your purchase price of {purchase_price} has been logged!')


@bot.command(name='current_price', help='Logs current price of turnips')
async def current_price(ctx, current_price: int):
    username = ctx.author.strip('#')
    botfunctions.insertSell(current_price, username)
    await ctx.send(f'@{username} Your current price of {current_price} has been logged!')

@bot.command(name='get_price', help='Displays the top prices for today')
async def get_price(ctx):
    return_prices = botfunctions.getPrices()
    await ctx.send(f'Here are the top prices for today:\n {return_prices}')

# Context.guild to fetch the Guild of the command, if any.
# Context.message to fetch the Message of the command.
# Context.author to fetch the Member or User that called the command.
# Context.send() to send a message to the channel the command was used in.

bot.run(TOKEN)