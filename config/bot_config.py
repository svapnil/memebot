from client.league import LeagueClient
from client.meme import MemeClient

GM_REGEX_TO_ACTION = {
    # display summary of most recent game
    "/gamesummary (.*)" : LeagueClient.display_game_summary,
    # display best champs for a summoner
    "/bestchamps (.*)" : LeagueClient.display_best_champs,
    # display match history for a summoner
    "/matchhistory (.*)" : LeagueClient.display_match_history,
    # display manual of all possible regexes
    "/memehelp" : MemeClient.display_meme_help,
    # display manual for whisper help
    "/whisperhelp" : MemeClient.display_whisper_help,
    # displays a pregame summary with ranks and champions of summoners
    "/pregamesummary" : LeagueClient.display_game_pregame_summary,
    # saves a meme to mp3
    "/play\s([a-zA-Z0-9_:/.?=]+)" : MemeClient.play_youtube,
    # if all else fails, try to play a meme
    ".*" : MemeClient.play_meme
}