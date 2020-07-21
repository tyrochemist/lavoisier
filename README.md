# lavoisier

A simple discord bot for fetching chemical data.

## Instructions

* Make sure you have pip or pipenv installed.
* Clone this repo.
* Create a discord application (and make it a bot) through here: https://discord.com/developers/applications
* Invite the new bot to your server with: https://discord.com/api/oauth2/authorize?client_id=CLIENT_ID&permissions=2048&scope=bot where `CLIENT_ID`is your application's CLIENT_ID.
* Get your bot's token.
* Replace the text "CLIENT_TOKEN" in the lavoisier_bot.py file with your client token.
* Go to https://developer.rsc.org/apis and sign up for an account, then click the "My Keys" page and then "Add a New Key". Enter a name for the key and select the Compounds v1 option, then create key.
* Replace the text "CHEMSPIDER_API_KEY" with your key text in the util.py file.
* In a terminal in the source directory, run `pip3 install -r requirements.txt`or, if you have pipenv installed, `pipenv install`.
* Run lavoisier_bot.py. 

## Commands

* `!chem compound name` will post an image url (which automatically embeds the image) of the named compound. 