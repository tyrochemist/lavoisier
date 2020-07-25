import discord
from chemspipy import ChemSpider
import util

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(
        client))  # Notifies console of login


@client.event
async def on_message(message):
    if message.author == client.user:  # Makes sure message sender is not bot itself
        return

    if message.content.startswith("!chem"):
        cname = util.remove_prefix(message)  # Removes prefix
        # Does search on name, returns first result as compound object
        comp = util.getCompound(cname)
        # Sends image URL as message, which becomes image embed
        await message.channel.send(comp.image_url)


client.run("CLIENT_TOKEN")
