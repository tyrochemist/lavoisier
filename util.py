from chemspipy import ChemSpider

cs = ChemSpider("CHEMSPIDER_API_KEY")


def remove_prefix(disctext):
    """Removes the command prefix from the passed string"""
    cprefix = "!chem "
    if disctext.content.startswith(cprefix):
        return disctext.content[len(cprefix):]


def getCompound(id):
    """Gets a compound object from a compound name or id"""
    slist = cs.search(id)  # Returns list of compounds
    compound = slist[0]  # Fetches top item of list as compound object
    return compound
