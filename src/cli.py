import asyncio
import tempfile
from pathlib import Path

import click

from downloader import Downloader
from ffmpeg.ffmpeg import FFmpeg
from kinescope.kinescope import Kinescope, KinescopeQuality
from sponsr.sponsr_auth import SponsrAuth
from sponsr.sponsr_grabber import SponsrGrabber
from sponsr.sponsr_post import SponsrPostPreview


@click.group("dump")
def cli() -> None:
    ...


@cli.command()
@click.option("--url", "-url", required=True, help='URL видео на test_sponsr.ru.')
@click.option('--dest-dir', "-d",
              type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True),
              help="Директория для загрузки файла")
@click.option('--auth', "-a", required=True, type=click.Path(exists=True, file_okay=True, dir_okay=False))
def video(url: str, dest_dir: str, auth: str) -> None:
    """Сохраняет видео по указанному url в директорию dest."""
    asyncio.run(save_video(url, Path(dest_dir), auth))


async def save_video(url: str, dest_dir: Path, auth: str) -> None:
    """Сохраняет видео по указанному url в директорию dest."""
    with tempfile.TemporaryDirectory() as temp_dir:
        await Downloader(
            SponsrGrabber(
                SponsrAuth(Path(auth))
            ),
            Kinescope(
                KinescopeQuality.THE_BEST,
                Path(temp_dir)
            ),
            FFmpeg(),
            dest_dir,
        ).download(url)


if __name__ == '__main__':
    cli()
