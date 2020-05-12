# TODO:
#   - suggestion box
#   - thanks for the follow (anon)
#   - check out this streamer! (link)
#   - Joel's on (StreamChanged)
#   - clear screen
#   - mod commands
#   X Available games list
#   X List of !commands
#   - Offline uptime fix
#   - !mods alert ping
#   - (embedded) Captions On request
#   - activity feed redemption





import os # for importing env vars for the bot to use
import time as builtintime
import datetime
import math
import asyncio
import random
from twitchio.ext import commands

from dotenv import load_dotenv
load_dotenv()


bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me says 'Trans rights!'")
    await waterboyprog(ws)



@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return
    
    # await ctx.channel.send(ctx.content) # repeat last message

    await bot.handle_commands(ctx)
    
    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")
    
    

@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')

@bot.command(name='time')
async def time(ctx):
        await ctx.send(builtintime.strftime("%b %e, %l:%M %p"))


@bot.command(name='uptime')
async def uptime(ctx):
    islive = await bot.get_stream("hackoon_")

    print(uptime)
    if islive is None:
        print("not live!!!!")
        await ctx.send("hackoon_ is not live.")
    else:
        print("live now!!!!")
        #await ctx.send(f"hackoon_ started at {islive['started_at']}")
    
        current_time = datetime.datetime.now(tz=datetime.timezone.utc)
        started_time = datetime.datetime.fromisoformat(f"{islive['started_at'][:-1]}+00:00")

        elapsed_time = current_time - started_time
        total_seconds = elapsed_time.total_seconds()
        uphours = int(total_seconds)//3600
        upminutes = int( ( (total_seconds) - ( (int( total_seconds ) // 3600 ) * 3600 )) // 60)
        await ctx.send(f"hackoon_ has been live for {uphours:02}:{upminutes:02} ")

#@bot.command(name='about')
#async def about(ctx):
#    await ctx.send('hackoon_ lives in california')

@bot.command(name='games')
async def games(ctx):
    gamelist = [
                'Avadon: The Black Fortress',
                'Caves of Qud',
                'DemonCrawl',
                'Doom 2016',
                'Doom 1993',
                'Dungeon Crawl Stone Soup',
                'Final Fantasy XIV',
                'Gladiabots',
                'Higurashi When They Cry',
                'HyperRogue',
                'Magic The Gathering Arena',
                'Quake 1',
                'Shadowrun Returns',
                'Shenzhen I/O',
                'Stoneshard',
                'System Shock: Enhanced Edition',
                'TIS-100',
                'Wizardry 6, Bane of the Cosmic Forge',
                'Wizardry 7, Crusaders of the Dark Savant',
                'Wizardry 8',
                'Xenonauts',
                'Emulated retro garbage!',
                'Neverwinter Nights: Enhanced Edition',
                'Icewind Dale: Enhanced Edition',
                'Pillars of Eternity',
                'Risk of Rain 2',
                'Torment: Tides of Numenera',
                'Golf With Your Friends',
                'Mindustry',
                'Dwarf Fortress',
                'XCOM 2'
                ]
    await ctx.send(f"here's a random sample of a few games hackoon_ has available to play: {str(random.sample(gamelist, 3))}")

async def waterboyprog(ws):
    waterboyprog = await bot.get_stream("hackoon_")
    while waterboyprog is not None:
        await ws.send_privmsg(os.environ['CHANNEL'], f"/me says 'Drink some water!'")
        await asyncio.sleep(3600/2)



@bot.command(name='commands')
async def commands(ctx):
    await ctx.send("!games, !uptime, !time, !test")





if __name__ == "__main__":
    bot.run()



