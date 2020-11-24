from client.league import LeagueClient
from client.meme import MemeClient

REGEX_TO_FUNCTION = {
    # display summary of most recent game
    "/gamessummary (.*)" : LeagueClient.display_game_summary,
    # display best champs for a champion
    "/bestchamps (.*)" : LeagueClient.display_best_champs,
    # display manual of all possible regexes
    "/memehelp" : MemeClient.display_meme_help,
    # if all else fails, try to play a meme
    ".*" : MemeClient.play_meme
}