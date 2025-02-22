from pathlib import Path

from ffmpeg.ffmpeg import FFmpeg
from kinescope.kinescope import Kinescope
from sponsr.sponsr_grabber import SponsrGrabber
from sponsr.sponsr_post import SponsrPostPreview


class Downloader:
    """Загружает видеоматериалы """
    def __init__(self, grabber: SponsrGrabber, kinescope: Kinescope, ffmpeg: FFmpeg, dest_dir: Path):
        self.grabber = grabber
        self.kinescope = kinescope
        self.ffmpeg = ffmpeg
        self.dest_dir = dest_dir

    def filename(self, post: SponsrPostPreview, video_counter: int) -> Path:
        counter = "" if video_counter == 0 else f"({video_counter})"
        filename = post.title.rstrip(". ") + counter + ".mp4"
        return self.dest_dir / filename

    async def download(self, url: str) -> None:
        for post in await self.grabber.posts(url):
            for i, video_id in enumerate(post.video_ids()):
                downloads = await self.kinescope.download(video_id)
                self.ffmpeg.concat(downloads.video, downloads.audio, self.filename(post, i))
