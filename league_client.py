from discord import Message
import re
from cassiopeia import Summoner

class LeagueClient:
    @staticmethod
    async def display_game_summary(message : Message):
            summoner_name = re.compile("/gamesummary (.*)").match(message.content).group(1)
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
