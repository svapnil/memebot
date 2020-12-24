from models.meme_model import Meme

REGEX_TO_MEME = {
   ".*(barber|holy smokes).*" : Meme(clip_url="clips/shoutoutbarber.mp3", title="Shoutout to my Barber"),
   ".*big (dog|dawg).*" : Meme(clip_url="clips/whatupbigdawgs.mp3", title="Marcin's Intro"),
   ".*best friends?.*" : Meme(clip_url="clips/twoprettybestfriends.mp3", title="Two Pretty Best Friends"),
   ".*pog.*" : Meme(clip_url="clips/faker.mp3", title="Faker"),
   ".*penta.*" : Meme(clip_url="clips/penta.mp3", title="Pentakill"),
   ".*quadra.*" : Meme(clip_url="clips/quadra.mp3", title="Quadrakill"),
   "(^gg$|.*mission failed.*)" : Meme(clip_url="clips/missionfailed.mp3", title="Mission Failed"),
   ".*bababooey.*" : Meme(clip_url="clips/bababooey.mp3", title="Bababooey"),
   ".*oof.*" : Meme(clip_url="clips/oof.mp3", title="Minecraft Noise"),
   ".*shit.*": Meme(clip_url="clips/awshit.mp3", title="Shit"),
   ".*calm down.*" : Meme(clip_url="clips/calm_down.mp3", title="Calm Down"),
   ".*pierre.*" : Meme(clip_url="clips/yo-pierre.mp3", title="Yo Pierre"),
   ".*perfect.*" : Meme(clip_url="clips/perfect.mp3", title="Perfect"),
   ".*pirate.*" : Meme(clip_url="clips/pirate.mp3", title="You Are A Pirate")
}