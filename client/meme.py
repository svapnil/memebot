from discord import VoiceChannel, Message, Member
import discord
import re
import asyncio
from config.meme import REGEX_TO_MEME

class MemeClient:
    @staticmethod
    async def play_meme(message: Message):
        content = message.content
        for regex, meme in REGEX_TO_MEME.items():
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
                audio = discord.FFmpegPCMAudio(meme.clip_url)
                voice.play(audio)
                print(f'Playing {regex}')
                while(voice.is_playing()):
                    await asyncio.sleep(1)
                await voice.disconnect()
                break

    @staticmethod
    async def display_meme_help(message: Message):
        memehelp = "**Messages that will play audio clips:**\n"
        for regex,_ in REGEX_TO_MEME.items():
            regex = regex[2:-2].replace('|',' or ')
            pattern = re.compile('[^a-zA-Z\d\s\)\()]')
            regex = re.sub(pattern,'',regex)
            memehelp = memehelp + regex + "\n"
            
        await message.channel.send(memehelp)
        print("Outputting Meme Help")
