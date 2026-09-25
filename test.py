from utils.audio_processor import process_input
from core.transcriber import transcribe_all

source = 'https://youtu.be/T-D1OfcDW1M?si=Yt7GnQuUqEeKbiI3'

chunks = process_input(source)
print(transcribe_all(chunks))