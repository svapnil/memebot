from config.bot import REGEX_TO_ACTION
from discord import Client, File
from discord.errors import ClientException
import re

class MemeBotClient(Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        try:
            for regex, action in REGEX_TO_ACTION.items():
                if re.search(regex, message.content.lower()):
                    await action(message)
        except ClientException as ce:
            if str(ce) == "Already connected to a voice channel.":
                await message.channel.send(file=File('pics/slowDownNeighbor.jpg'))
                print("Voice channel already active, asking user to slow down")
            else:
                await message.channel.send("I\'m kinda confused right now bruh")
                print(f'Unknown ClientExceptionError: {ce}')
        except Exception as e:
            await message.channel.send("I\'m kinda confused right now bruh")
            print(f'Unknown Exception occured: {e}')
        