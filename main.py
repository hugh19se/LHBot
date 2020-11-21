import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
import random

bot = discord.Client()

bot = commands.Bot(command_prefix='.')

@bot.command()
async def say(ctx):
    await ctx.message.delete()
    x = ctx.message.content
    await ctx.send(x[4:])

@bot.command()
async def purge(ctx):
    await ctx.channel.purge()

bot.run('api_token_goes_here')

