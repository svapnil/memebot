from cassiopeia.core.match import Participant
from merakicommons.container import LazyList 

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
        for player in team:
            info += LeagueClientHelper.display_summoner_info(player)
        return info