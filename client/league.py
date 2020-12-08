from discord import Message
from helper.league import LeagueClientHelper
from utils.logger import Logger
import re
from cassiopeia import Summoner
from cassiopeia.data import GameMode

def format_game_mode(mode : GameMode) -> str:
    # "GameMode.aram" -> "ARAM"
    return str(mode)[9:].upper()
class LeagueClient:
    @staticmethod
    async def display_game_summary(message : Message) -> None:
        summoner_name = re.compile("/gamesummary (.*)").match(message.content).group(1)
        summoner = Summoner(name=summoner_name, region="NA")
        player_match_history = summoner.match_history()
        
        output = "```"
        output += "{:>18} {:>14} {:>14} {:>15} {:>16}".format("SUMMONER", 
                                                                "KILLS", 
                                                                "DEATHS", 
                                                                "ASSISTS", 
                                                                "KDA") + "\n"
        output += LeagueClientHelper.display_team_info(player_match_history[0].blue_team.participants)
        output += "----------------------------------------------------------------------------------\n"
        output += LeagueClientHelper.display_team_info(player_match_history[0].red_team.participants)

        output += "```"
        await message.channel.send(output)
        Logger.log('Outputting Game Summary for: {summoner_name}')  
            
    @staticmethod
    async def display_best_champs(message : Message) -> None:
        summoner_name = message.content[12:]
        bestchamps_message ="**Best champs for " + summoner_name + ":**\n"
        summoner = Summoner(name=summoner_name, region="NA")
        good_with = summoner.champion_masteries.filter(lambda cm: cm.level >=5)
        bestchamps_message += ", ".join([cm.champion.name for cm in good_with])
        await message.channel.send(bestchamps_message)
        Logger.log("Outputting Best Champ")
    
    @staticmethod
    async def display_match_history(message : Message) -> None:
        summoner_name = message.content[14:]
        summoner = Summoner(name=summoner_name, region="NA")
        history = summoner.match_history[:5]
        output = "{:>8} {:>14} {:>14} {:>14} {:>15} {:>16}".format(
                                                    "MODE",
                                                    "CHAMPION",
                                                    "KILLS",
                                                    "DEATHS",
                                                    "ASSISTS",
                                                    "KDA") + "\n" 
        for match in history:
            for player in match.participants:
                if player.summoner.id == summoner.id:
                    kills = player.stats.kills
                    deaths = player.stats.deaths
                    assists = player.stats.assists
                    kda = str(round(player.stats.kda, 2))
                    output += "{:>8} {:>14} {:>14} {:>14} {:>15} {:>16}".format(
                                                                format_game_mode(match.mode),
                                                                player.champion.name,
                                                                kills,
                                                                deaths,
                                                                assists,
                                                                kda) + "\n" 
                    
        await message.channel.send(f'**Last 5 Games for {summoner.name}:**```{output}```')
        Logger.log("Outputting Match History")