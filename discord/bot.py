import os
from os import getenv
import discord
from discord.ext import commands
from discord.modules.helpers import *

from dotenv import load_dotenv
load_dotenv(override=True)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(
    command_prefix=PREFIX,
    owner_ids=OWNER_IDS,
    intents=discord.Intents.all()
)

bot.remove_command('help')

for filename in os.listdir(COG_FOLDER):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('TOKEN')