import os
from static_ffmpeg import run


def setup_ffmpeg():

    ffmpeg_path, ffprobe_path = (
        run.get_or_fetch_platform_executables_else_raise()
    )

    os.environ["PATH"] = (
        os.path.dirname(ffmpeg_path)
        + os.pathsep
        + os.environ["PATH"]
    )