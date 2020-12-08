from cassiopeia import Summoner
from cassiopeia.core.match import Participant
from merakicommons.container import LazyList 
from cassiopeia.data import GameMode

def get_kda(p):
   return p.stats.kda 

def format_game_mode(mode : GameMode) -> str:
    # "GameMode.aram" -> "ARAM"
    return str(mode)[9:].upper()

class LeagueClientHelper:
    @staticmethod
    def display_summoner_info(player : Participant) -> str:
        name = player.summoner.name
        kills = player.stats.kills
        deaths = player.stats.deaths
        assists = player.stats.assists
        kda = str(round(player.stats.kda, 2))

        return "{:>18} {:>14} {:>14} {:>15} {:>16}".format(name,
                                                        kills,
                                                        deaths,
                                                        assists,
                                                        kda) + "\n" 
    @staticmethod
    def display_team_info(team : LazyList) -> str:
        info = ""
        players = [p for p in team]
        # sort by highest kda first, descending
        players.sort(key=get_kda)
        players.reverse()
        for player in players:
            info += LeagueClientHelper.display_summoner_info(player)
        return info

    @staticmethod
    def display_match_history_info(summoner : Summoner, history : LazyList) -> str:
        output = ""
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
        return output
        