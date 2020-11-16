import discord
import ctypes.util
import os
from meme import MemePlayer

def load_opus():
    if not discord.opus.is_loaded():
        opus_path = ctypes.util.find_library("opus")
        discord.opus.load_opus(opus_path)


class MemeBotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        guild = message.guild
        # making the assumption that users are in the first channel
        channel = guild.voice_channels[0]
        await MemePlayer.play_meme(channel, message.content)
        
load_opus()
client = MemeBotClient()
DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']
client.run(DISCORD_BOT_TOKEN)

# Code Dump:
# await message.channel.send("shoutout to my barber " + str(message.author.nick), tts=True)
# for vc in guild.voice_channels:
#    if len(vc.members) > len(channel.members):
#         channel = vc