from cassiopeia.core.match import Participant
from merakicommons.container import LazyList 
from cassiopeia.data import Queue
def get_kda(p):
   return p.stats.kda 

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