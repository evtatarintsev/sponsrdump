import tempfile
from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path


class KinescopeQuality(Enum):
    "640x360"
    THE_BEST = auto()


@dataclass
class KinescopeDownloads:
    """Результат скачивания артефактов с kinescope.io"""
    video: Path
    audio: Path


class Kinescope:
    def __init__(self, quality: KinescopeQuality, dest_dir: Path):
        self.quality = quality
        self.dest_dir = dest_dir

    async def download(self, file_id: str) -> KinescopeDownloads:
        return KinescopeDownloads(video=Path(), audio=Path())
