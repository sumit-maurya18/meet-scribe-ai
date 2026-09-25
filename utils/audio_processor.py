# ============================================================
# DEVELOPMENT-ONLY SETUP
# ============================================================
# DELETE THIS ENTIRE SECTION LATER when FFmpeg initialization
# is moved to app.py / main.py.
# ============================================================

import os
import sys

# Allow this file to find the project-level "config" folder
# when running:
# python utils/audio_processor.py
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, PROJECT_ROOT)

# Initialize FFmpeg before importing pydub.
from config.ffmpeg import setup_ffmpeg

setup_ffmpeg()


# ============================================================

import yt_dlp
from pydub import AudioSegment  # used in chunking

# Folder to save input resources
DOWNLOAD_DIR = "downloads"

os.makedirs(
    DOWNLOAD_DIR,
    exist_ok=True
)


def download_youtube_audio(url: str) -> str:

    output_path = os.path.join(
        DOWNLOAD_DIR,
        "%(title)s.%(ext)s"
    )

    ydl_opts = {
        "format": "bestaudio/best",

        "outtmpl": output_path,

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],

        "quiet": True  # suppress download progress/info
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(
            url,
            download=True
        )

        # Changed only because this is safer than assuming
        # the source extension is .webm or .m4a.
        filename = (
            os.path.splitext(
                ydl.prepare_filename(info)
            )[0]
            + ".wav"
        )

    return filename

# data = download_youtube_audio('https://youtu.be/DvD6SANAJ_0?si=Om1hOz3366bIByw3')

def convert_to_wav(input_path : str) -> str:
    #convert audio/video file to WAV format using pydub
    
    output_path = os.path.splitext(input_path)[0] + '_converted.wav'
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(output_path, format='wav')
    
    return output_path

# data_final = convert_to_wav(data)

def chunk_audio(wav_path : str, chunk_minutes : int = 10) -> list:
    audio = AudioSegment.from_wav(wav_path)
    chunk_ms = chunk_minutes * 60 * 1000
    
    chunks = []
    
    for i, start in enumerate(range(0, len(audio), chunk_ms)):
        chunk = audio[start : start + chunk_ms]
        chunk_path = f'{wav_path}_chunk_{i}.wav'
        chunk.export(chunk_path, format = 'wav')
        
        chunks.append(chunk_path)
        
    return chunks

# print(chunk_audio(data_final))

def process_input(source : str) -> list:
    
    if source.startswith('http://') or source.startswith('https://'):
        print('Detected YouTube URL. Downloading audio...')
        wav_path = download_youtube_audio(source)
    
    else:
        print('Detected local file. Converting to WAV...')
        wav_path = convert_to_wav(source)
        
    print('Chunking audio...')
    chunks = chunk_audio(wav_path)
    print(f'Audio ready - {len(chunks)} chunks(s) created.')
    return chunks

# process_input('https://youtu.be/DvD6SANAJ_0?si=Om1hOz3366bIByw3')


# ============================================================
# DEVELOPMENT TEST
# ============================================================

# if __name__ == "__main__":

#     print(
#         download_youtube_audio(
#             "https://youtu.be/liTfD88dbCo?si=Srcz5TrpXwTGsIU3"
#         )
#     )