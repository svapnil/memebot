from cassiopeia.core.match import Participant
from merakicommons.container import LazyList 

def get_kda(p):
   return p.stats.kda 

class LeagueClientHelper:
    @staticmethod
    def display_summoner_info(player : Participant):
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
    def display_team_info(team : LazyList):
        info = ""
        players = [p for p in team]
        # sort by highest kda first, descending
        players.sort(key=get_kda)
        players.reverse()
        for player in players:
            info += LeagueClientHelper.display_summoner_info(player)
        return info