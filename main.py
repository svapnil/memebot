import discord
import asyncio
import ctypes.util
import os
import re

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

        if re.search(".*(barber|holy smokes).*", message.content):
            guild = message.guild
            # expect there to be atleast one voice channel 
            channel = guild.voice_channels[1]
            # for vc in guild.voice_channels:
            #    if len(vc.members) > len(channel.members):
            #         channel = vc
            voice = await channel.connect()
            audio = discord.FFmpegPCMAudio("shoutoutbarber.mp3")
            voice.play(audio)
            while(voice.is_playing()):
                await asyncio.sleep(1)
            await voice.disconnect()
        
load_opus()
client = MemeBotClient()
DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']
client.run(DISCORD_BOT_TOKEN)

# Code Dump:
# await message.channel.send("shoutout to my barber " + str(message.author.nick), tts=True)