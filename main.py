from voice_to_text import *
from record_voice import *

record_voice()

filename = "audio.m4a"
audio_url = upload(filename)

save_transcript(audio_url, 'audio_text')