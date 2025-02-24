from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Generator

from ffmpeg.ffmpeg import FFmpeg
from kinescope.kinescope import Kinescope
from sponsr.sponsr_grabber import SponsrGrabber
from sponsr.sponsr_post import SponsrPostPreview


class Downloader:
    """Загружает видеоматериалы """

    def __init__(
            self,
            grabber: SponsrGrabber,
            kinescope: Kinescope,
            ffmpeg: FFmpeg,
            dest_dir: Path,
            progress: Path,
            concurrency: int
    ):
        self.grabber = grabber
        self.kinescope = kinescope
        self.ffmpeg = ffmpeg
        self.dest_dir = dest_dir
        self.progress = progress
        self.concurrency = concurrency

    def filename(self, post: SponsrPostPreview, video_counter: int) -> Path:
        counter = "" if video_counter == 0 else f"({video_counter})"
        filename = post.title.rstrip(". ") + counter + ".mp4"
        return self.dest_dir / filename

    async def download(self, url: str) -> None:
        print("Начинаем скачивание материалов")
        try:
            posts = await self.grabber.posts(url)
        except Exception as e:
            print("Не удалось получить список постов в проекте")
            return

        with progress_logger(self.progress) as ready_ids:
            for post in posts:
                print("=" * 50)
                if post.id not in ready_ids:
                    print(f"Скачиваем '{post.title}'...")
                    try:
                        await self.download_post(post)
                        ready_ids.add(post.id)
                        print(f"'{post.title}' скачан.")
                    except Exception as exc:
                        print(f"При скачивании '{post.title}' произошла ошибка: {exc}")
                else:
                    print(f"'{post.title}' был скачан ранее.")

    async def download_post(self, post: SponsrPostPreview) -> None:
        for i, video_id in enumerate(post.video_ids()):
            downloads = await self.kinescope.download(video_id)
            self.ffmpeg.concat(downloads.video, downloads.audio, self.filename(post, i))


@contextmanager
def progress_logger(file: Path) -> Generator[set[int]]:
    ready_ids: set[int] = set()
    if file.exists():
        with file.open() as f:
            ready_ids = {int(line) for line in f.readlines()}

    try:
        yield ready_ids
    finally:
        with file.open("w") as f:
            f.writelines([f"{id}\n" for id in sorted(ready_ids)])
