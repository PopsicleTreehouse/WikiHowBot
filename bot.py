import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from whrequests import search as whs

bot = commands.Bot(command_prefix="wh!")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=bot.command_prefix+"help"))


@bot.command(name="search", brief="Searches wikihow for term(s)")
async def search(ctx, *, term=None):
    if(term is None):
        ctx.send("Enter a valid search term.")
    await ctx.reply(whs(term, max_results=1), mention_author=True)

load_dotenv()
bot.run(getenv('TOKEN'))
