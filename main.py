from voice_to_text import *
from record_voice import *


# Transcription section
seconds = 6

record_voice(seconds)

filename = "audio.m4a"
audio_url = upload(filename)

save_transcript(audio_url, 'audio_text', seconds)

# Model section