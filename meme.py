from discord import VoiceChannel
import discord
import re
import asyncio

REGEX_TO_MEME = {
   ".*(barber|holy smokes).*" : "shoutoutbarber.mp3",
   ".*big (dog|dawg).*" : "whatupbigdawgs.mp3"
}

class MemePlayer:
    @staticmethod
    async def play_meme(channel: VoiceChannel, content: str):
        for regex, sound_url in REGEX_TO_MEME.items():
            if re.search(regex, content):
                voice = await channel.connect()
                audio = discord.FFmpegPCMAudio(sound_url)
                voice.play(audio)
                while(voice.is_playing()):
                    await asyncio.sleep(1)
                await voice.disconnect()
                break