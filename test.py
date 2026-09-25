# from utils.audio_processor import process_input
# from core.transcriber import transcribe_all

# source = 'https://youtu.be/T-D1OfcDW1M?si=Yt7GnQuUqEeKbiI3'

# chunks = process_input(source)
# print(transcribe_all(chunks))

from dotenv import load_dotenv
import os
load_dotenv()
from utils.audio_processor import process_input
from core.transcriber import transcribe_all

# print('KEY LOADED', os.getenv('SARVAM_API_KEY')) #key debug
# print('CWD:', os.getcwd())

source = 'https://youtu.be/TOHuYdr6Y0U?si=LC5dHm1ZJcU-OERB'
language = 'hinglish'

chunks = process_input(source)
transcript = transcribe_all(chunks, language = language)
print("\n=== TRANSCRIPT ===\n")
print(transcript)