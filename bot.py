import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from whapi import search

bot = commands.Bot(command_prefix="wh!")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=bot.command_prefix+"help"))


@bot.command(name="search", brief="Searches wikihow for term")
async def search(ctx, term):
    await ctx.send(search(term)["url"])

load_dotenv()
bot.run(getenv('TOKEN'))
