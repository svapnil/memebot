from models.meme import Meme

REGEX_TO_MEME = {
   ".*(barber|holy smokes).*" : Meme(clip_url="clips/shoutoutbarber.mp3"),
   ".*big (dog|dawg).*" : Meme(clip_url="clips/whatupbigdawgs.mp3"),
   ".*best friends?.*" : Meme(clip_url="clips/twoprettybestfriends.mp3"),
   ".*pog.*" : Meme(clip_url="clips/faker.mp3"),
   ".*penta.*" : Meme(clip_url="clips/penta.mp3"),
   ".*quadra.*" : Meme(clip_url="clips/quadra.mp3"),
   "(^gg$|.*mission failed.*)" : Meme(clip_url="clips/missionfailed.mp3"),
   ".*bababooey.*" : Meme(clip_url="clips/bababooey.mp3"),
   ".*oof.*" : Meme(clip_url="clips/oof.mp3"),
   ".*shit.*": Meme(clip_url="clips/awshit.mp3"),
   ".*calm down.*" : Meme(clip_url="clips/calm_down.mp3"),
   ".*pierre.*" : Meme(clip_url="clips/yo-pierre.mp3"),
   ".*perfect.*" : Meme(clip_url="clips/perfect.mp3"),
   ".*pirate.*" : Meme(clip_url="clips/pirate.mp3"),
   ".*mario judah.*" : Meme(clip_url="clips/whereismariojudah.mp3")
}