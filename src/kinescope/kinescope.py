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
        print(mpd.video(self.quality))
        return KinescopeDownloads(video=Path(), audio=Path())
