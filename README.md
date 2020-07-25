# lavoisier

A simple discord bot for fetching chemical data.

## Instructions

This repo utilizes a variety of dependencies (working on pruning this) and works best when run in a virtual environment created through conda or pip. 

* Clone this repo. If using conda, run `conda env creatae --file environment.yaml`. Otherwise, use whatever you would like to create a virtual environment, then run `pip3 install -r requirements.txt`.
* Create a discord application (and make it a bot) through here: https://discord.com/developers/applications
* Invite the new bot to your server with: https://discord.com/api/oauth2/authorize?client_id=CLIENT_ID&permissions=2048&scope=bot where `CLIENT_ID`is your application's CLIENT_ID.
* Get your bot's token.
* Replace the text "CLIENT_TOKEN" in the lavoisier_bot.py file with your client token.
* Go to https://developer.rsc.org/apis and sign up for an account, then click the "My Keys" page and then "Add a New Key". Enter a name for the key and select the Compounds v1 option, then create key.
* Replace the text "CHEMSPIDER_API_KEY" with your key text in the util.py file.
* Run lavoisier_bot.py. 

## Commands

* `!chem compound name` will post an image url (which automatically embeds the image) of the named compound. 