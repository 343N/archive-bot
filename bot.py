import math
import discord
import json
import requests
import time

from archiver.MessageHistoryHandler import MessageHistoryHandler

GUILD = 316070711284465665
GUILD2 = 1022401755646005298
TOKENS = json.load(open("tokens.json", 'r'))

bot = discord.Bot()

FINSIHED_STR = []

@bot.event
async def on_ready():
    print(f"we have logged in {bot.user}")

@bot.slash_command(guild_ids=[GUILD, GUILD2])
async def archive(ctx):
    # print(ctx)
    res = await ctx.respond(content="i got you kid", file=discord.File('loading.gif'))
    mhh = MessageHistoryHandler(bot, ctx.channel)
    await mhh.getMessages()
    time.sleep(0.3)
    # await ctx.delete()
    await ctx.channel.send(file=discord.File('messages.json'))


def getRandomFact():
    r = requests.get('https://uselessfacts.jsph.pl/random.txt?language=en')
    prefix = "Did you know? "
    fact = str(r.content, 'utf8').split('\n')[0][2:].replace('`', '\'')
    return f"{prefix}{fact}"

bot.run(TOKENS["BOT_TOKEN"])

