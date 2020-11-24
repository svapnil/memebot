import discord
from meme_player import MemePlayer
from meme_config import REGEX_TO_MEME
import re
from cassiopeia import Summoner

class MemeBotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return


        if re.search("/gamesummary (.*)", message.content):
            regex_match_rule = re.compile("/gamesummary (.*)")
            summoner_name = regex_match_rule.match(message.content).group(1)

            summoner = Summoner(name=summoner_name, region="NA")
            player_match_history = summoner.match_history()
            participants = {}
            
            printMessage = "```"

            printMessage += "{:>18} {:>14} {:>14} {:>15} {:>16}".format("SUMMONER", 
                                                                    "KILLS", 
                                                                    "DEATHS", 
                                                                    "ASSISTS", 
                                                                    "KDA") + "\n"


            for blue in player_match_history[0].blue_team.participants:
                player = player_match_history[0].blue_team.participants[blue]

                participants[player] = {}

                participants[player]['summoner_name'] = player.summoner.name
                participants[player]['kills'] = player.stats.kills
                participants[player]['deaths'] = player.stats.deaths
                participants[player]['assists'] = player.stats.assists
                participants[player]['KDA'] = str(round(player.stats.kda, 2))

                printMessage += "{:>18} {:>14} {:>14} {:>15} {:>16}".format(participants[player]['summoner_name'],
                                                                participants[player]['kills'],
                                                                participants[player]['deaths'],
                                                                participants[player]['assists'],
                                                                participants[player]['KDA']) + "\n" 

            printMessage += "----------------------------------------------------------------------------------\n"

            for red in player_match_history[0].red_team.participants:
                player = player_match_history[0].red_team.participants[red]

                participants[player] = {}

                participants[player]['summoner_name'] = player.summoner.name
                participants[player]['kills'] = player.stats.kills
                participants[player]['deaths'] = player.stats.deaths
                participants[player]['assists'] = player.stats.assists
                participants[player]['KDA'] = str(round(player.stats.kda, 2))

                printMessage += "{:>18} {:>14} {:>14} {:>15} {:>16}".format(participants[player]['summoner_name'],
                                                            participants[player]['kills'],
                                                            participants[player]['deaths'],
                                                            participants[player]['assists'],
                                                            participants[player]['KDA']) + "\n"

            printMessage += "```"
            await message.channel.send(printMessage)
            print("Outputting Game Summary for: ",  summoner_name)


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
        