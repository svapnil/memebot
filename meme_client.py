from discord import VoiceChannel, Message, Member
import discord
import re
import asyncio
from meme_config import REGEX_TO_MEME

class MemeClient:
    @staticmethod
    async def play_meme(message: Message):
        content = message.content
        for regex, sound_url in REGEX_TO_MEME.items():
            if re.search(regex, content.lower()):
                channel = None
                if isinstance(message.author, Member): 
                    if message.author.voice and message.author.voice.channel:
                        channel = message.author.voice.channel
                    else:
                        name = message.author.nick or message.author.name
                        await message.channel.send(f'You\'re not in a Discord channel neighbor {name}!')             
                        return
                voice = await channel.connect()
                audio = discord.FFmpegPCMAudio(sound_url)
                voice.play(audio)
                print(f'Playing {regex}')
                while(voice.is_playing()):
                    await asyncio.sleep(1)
                await voice.disconnect()
                break