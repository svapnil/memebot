import discord
from discord import Member
import ctypes.util
import os
from meme_bot_client import MemeBotClient

def load_opus():
    if not discord.opus.is_loaded():
        opus_path = ctypes.util.find_library("opus")
        discord.opus.load_opus(opus_path)

if __name__ == "__main__":
    load_opus()
    client = MemeBotClient()
    DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']
    client.run(DISCORD_BOT_TOKEN)

# Code Dump:
# await message.channel.send("shoutout to my barber " + str(message.author.nick), tts=True)
# for vc in guild.voice_channels:
#    if len(vc.members) > len(channel.members):
#         channel = vc