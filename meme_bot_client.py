import discord
from meme_player import MemePlayer

class MemeBotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        try:
            await MemePlayer.play_meme(message)
        except discord.errors.ClientException:
            await message.channel.send("Slow down neighbor")
        except Exception as e:
            print(e)
        