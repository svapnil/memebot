from discord import FFmpegPCMAudio

class Meme:
    def __init__(self, clip_url: str, help_text=None):
        self.clip_url = clip_url
        self.help_text = help_text

    @property
    def audio(self):
        FFmpegPCMAudio(self.clip_url)
