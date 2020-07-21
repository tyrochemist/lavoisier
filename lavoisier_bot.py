import discord
from chemspipy import ChemSpider
import util

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!chem"):
        cname = util.remove_prefix(message)
        comp = util.getCompound(cname)
        await message.channel.send(comp.image_url)


client.run("CLIENT_TOKEN")
