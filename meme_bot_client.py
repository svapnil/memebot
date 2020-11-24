import discord
from meme_player import MemePlayer
from meme_config import REGEX_TO_MEME
from league_client import LeagueClient
from cassiopeia import Summoner
import re
class MemeBotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return


        if re.search("/gamesummary (.*)", message.content):
           await LeagueClient.display_game_summary(message)

        if re.search("/bestchamps (.*)", message.content):
            summoner_name = message.content[12:]
            bestchamps_message ="**Best champs for " + summoner_name + ":**\n"
            summoner = Summoner(name=summoner_name, region="NA")
            good_with = summoner.champion_masteries.filter(lambda cm: cm.level >=5)
            bestchamps_message += ", ".join([cm.champion.name for cm in good_with])
            await message.channel.send(bestchamps_message)
            print("Outputting Best Champ")
        
        # print manual of all possible regexes
        if message.content == '/memehelp':
            memehelp = "**Messages that will play audio clips:**\n"
            for regex,_ in REGEX_TO_MEME.items():
                regex = regex[2:-2].replace('|',' or ')
                pattern = re.compile('[^a-zA-Z\d\s\)\()]')
                regex = re.sub(pattern,'',regex)
                memehelp = memehelp + regex + "\n"
                
            await message.channel.send(memehelp)
            print("Outputting Meme Help")
            return
        
        # look for a meme to play
        try:
            await MemePlayer.play_meme(message)
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
        