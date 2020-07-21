from chemspipy import ChemSpider

cs = ChemSpider("CHEMSPIDER_API_KEY")


def remove_prefix(disctext):
    """Removes the command prefix from the passed string"""
    cprefix = "!chem "
    if disctext.content.startswith(cprefix):
        return disctext.content[len(cprefix):]

def getCompound(id):
    """Gets a compound object from a compound name or id"""
    slist = cs.search(id)
    compound = slist[0]
    return compound
