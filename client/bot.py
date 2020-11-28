from config.bot import REGEX_TO_ACTION
from discord import Client, File, DMChannel, FFmpegPCMAudio
from discord.errors import ClientException
from gtts import gTTS
import asyncio
import re

class MemeBotClient(Client):
    def __init__(self):
        self.voice_lookup = {}    
        super().__init__()

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_voice_state_update(self, member, before, after):
        # don't respond to ourselves
        if member.id == self.user.id:
            return
        print("voice state update")
        self.voice_lookup[member.id] = after.channel
        return

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        try:
            if isinstance(message.channel, DMChannel):
                if re.search("whisper", message.content.lower()):
                    payload = message.content[7:]
                    tts = gTTS(text=payload, lang="en", slow=False)
                    tts.save("_tts.mp3")
                    channel = self.voice_lookup.get(message.author.id)
                    if not channel:
                        await message.channel.send(f'Try rejoining the Discord channel and trying again my neighbor')             
                        return
                    voice = await channel.connect()
                    audio = FFmpegPCMAudio("_tts.mp3")
                    voice.play(audio)
                    print(f'Playing whisper')
                    print(f'Payload: {payload}')
                    print(f'From: {message.author.name}')
                    while(voice.is_playing()):
                        await asyncio.sleep(1)
                    await voice.disconnect()
                    return
            for regex, action in REGEX_TO_ACTION.items():
                if re.search(regex, message.content.lower()):
                    await action(message)
        except ClientException as ce:
            if str(ce) == "Already connected to a voice channel.":
                await message.channel.send(file=File('pics/slowDownNeighbor.jpg'))
                print("Voice channel already active, asking user to slow down")
            else:
                await message.channel.send("I\'m kinda confused right now bruh")
                print(f'Unknown ClientExceptionError: {ce}')
        except Exception as e:
            await message.channel.send("I\'m kinda confused right now bruh")
            print(f'Unknown Exception occured: {e}')
        