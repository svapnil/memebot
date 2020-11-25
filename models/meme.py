from discord import FFmpegPCMAudio

class Meme:
    def __init__(self, clip_url: str, title: str = None):
        self.clip_url = clip_url
        self.title = title

    @property
    def audio(self):
        return FFmpegPCMAudio(self.clip_url)
