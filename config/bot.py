from client.league import LeagueClient
from client.meme import MemeClient

GM_REGEX_TO_ACTION = {
    # display summary of most recent game
    "/gamesummary (.*)" : LeagueClient.display_game_summary,
    # display best champs for a champion
    "/bestchamps (.*)" : LeagueClient.display_best_champs,
    # display manual of all possible regexes
    "/memehelp" : MemeClient.display_meme_help,
    # display manual for whisper help
    "/whisperhelp" : MemeClient.display_whisper_help,
    # if all else fails, try to play a meme
    ".*" : MemeClient.play_meme
}