import os
from twitchio.ext import commands

# set up the bot
bot = commands.Bot(
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
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")
    
    if ('scooter' in ctx.content.lower()) or ('scottie' in ctx.content.lower()):
        await ctx.channel.send(f"Scooter bad!!! AHAHAHAAH XD XD")

    if ('kappa' in ctx.content.lower()):
        await ctx.channel.send(f"Kappa")

    if ('pog' in ctx.content.lower()):
        await ctx.channel.send(f"PogChamp")

    if ('nick' in ctx.content.lower()):
        await ctx.channel.send(f"Champion Ocean Best Player PogChamp OMG")

    if ('cade' in ctx.content.lower()):
        await ctx.channel.send(f"Wow coding genius and god on his quinary role wow BloodTrail Champion Ocean")

    if ('anthony' in ctx.content.lower()):
        await ctx.channel.send(f"10000 IQ Draven shitter BibleThump")

    if ('marshall' in ctx.content.lower()):
        await ctx.channel.send(f"Wow great streamer sexy beard man")


@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')


if __name__ == "__main__":
    bot.run()