from cassiopeia import Summoner
from cassiopeia.core.match import Participant
from merakicommons.container import LazyList 
from cassiopeia.data import GameMode
from cassiopeia.data import Queue

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
                    is_win = player.team.win
                    win_output = "WIN" if is_win else "LOSS"
                    output += "{:>8} {:>14} {:>14} {:>14} {:>15} {:>16} {:>6}".format(
                                                                format_game_mode(match.mode),
                                                                player.champion.name,
                                                                kills,
                                                                deaths,
                                                                assists,
                                                                kda,
                                                                win_output) + "\n" 
        return output
        
    
    @staticmethod
    def display_summoner_pregame_info(player : Participant) -> str:
        name = player.summoner.name
        champion = player.champion.name
        soloRank = ""

        flexRank = ""
        try:
            rank = [player.summoner.ranks[Queue.ranked_solo_fives].tier][0]
            divison = [player.summoner.ranks[Queue.ranked_solo_fives].division][0]
            soloRank = str(rank) + " " + str(divison)
        except:
            soloRank = "Not Ranked"
        try:
            rank = [player.summoner.ranks[Queue.ranked_flex_fives].tier][0]
            divison = [player.summoner.ranks[Queue.ranked_flex_fives].division][0]
            flexRank = str(rank) + " " + str(divison)
        except:
            flexRank = "Not Ranked"

        return "{:>18} {:>14} {:>14} {:>15}".format(name,
                                            champion,
                                            soloRank,
                                            flexRank) + "\n" 
    @staticmethod
    def display_team_pregame_info(team : LazyList) -> str:
        info = ""
        players = team
        for player in players:
            info += LeagueClientHelper.display_summoner_pregame_info(player)
        return info
