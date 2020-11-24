import discord
from .meme import MemeClient
from .config.meme import REGEX_TO_MEME
from .config.bot import REGEX_TO_FUNCTION
from .league import LeagueClient
from cassiopeia import Summoner
import re

class MemeBotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        try:
            for regex, function in REGEX_TO_FUNCTION.items():
                if re.search(regex, message.content.lower()):
                    await function(message)
        except discord.errors.ClientException as ce:
            if str(ce) == "Already connected to a voice channel.":
                await message.channel.send(file=discord.File('pics/slowDownNeighbor.jpg'))
                print("Voice channel already active, asking user to slow down")
            else:
                await message.channel.send("I\'m kinda confused right now bruh")
                print(f'Unknown ClientExceptionError: {ce}')
        except Exception as e:
            await message.channel.send("I\'m kinda confused right now bruh")
            print(f'Unknown Exception occured: {e}')
        