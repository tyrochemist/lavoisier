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
        compembed = discord.Embed(
            title=comp.common_name, color=discord.Colour.purple())
        compembed.set_image(url=comp.image_url)
        compembed.add_field(
            name="Formula", value=f"`{comp.molecular_formula}`")
        compembed.add_field(name="SMILES", value=comp.smiles)
        compembed.add_field(name="Molecular Weight",
                            value=comp.molecular_weight)
        compembed.add_field(
            name="URL", value=f"https://www.chemspider.com/Chemical-Structure.{comp.record_id}.html")
        await message.channel.send(embed=compembed)


client.run("CLIENT_TOKEN")
