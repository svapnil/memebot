import discord
from meme_player import MemePlayer
from meme_config import REGEX_TO_MEME

class MemeBotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        # print manual of all possible regexes
        if message.content == '/memehelp':
            memehelp = ""
            for regex,_ in REGEX_TO_MEME.items():
                memehelp = memehelp + regex[2:-2].replace('|',' or ') + "\n"
            await message.channel.send(memehelp)
            print("Outputting Meme Help")
            return
        
        # look for a meme to play
        try:
            await MemePlayer.play_meme(message)
        except discord.errors.ClientException:
            await message.channel.send(file=discord.File('pics/slowDownNeighbor.jpg'))
            print("Voice channel already active, asking user to slow down")
        except Exception as e:
            print(e)
        