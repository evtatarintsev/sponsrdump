from dataclasses import dataclass
from pathlib import Path

import httpx

from kinescope.master_mpd import MasterMpd
from kinescope.quality import KinescopeQuality


@dataclass
class KinescopeDownloads:
    """Результат скачивания артефактов с kinescope.io"""
    video: Path
    audio: Path


class Kinescope:
    headers={"Referer": "https://kinescope.io"}

    def __init__(self, quality: KinescopeQuality, dest_dir: Path):
        self.quality = quality
        self.dest_dir = dest_dir

    async def download(self, file_id: str) -> KinescopeDownloads:
        async with httpx.AsyncClient(headers=self.headers) as client:
            response = await client.get(f"https://kinescope.io/{file_id}/master.mpd")
            mpd = MasterMpd(response.text)

        video_file = self.dest_dir / f"{file_id}.video.mp4"
        with video_file.open("wb") as vf:
            async with httpx.AsyncClient(headers=self.headers) as client:
                for url in mpd.video(self.quality):
                    response = await client.get(url)
                    vf.write(response.content)

        audio_file = self.dest_dir / f"{file_id}.audio.mp4"
        with audio_file.open("wb") as af:
            async with httpx.AsyncClient(headers=self.headers) as client:
                for url in mpd.audio():
                    response = await client.get(url)
                    af.write(response.content)


        return KinescopeDownloads(video=video_file, audio=audio_file)
