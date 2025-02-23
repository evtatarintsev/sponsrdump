import asyncio
import tempfile
from pathlib import Path

import click

from downloader import Downloader
from ffmpeg.ffmpeg import FFmpeg
from kinescope.kinescope import Kinescope
from kinescope.quality import KinescopeQuality
from sponsr.sponsr_auth import SponsrAuth
from sponsr.sponsr_grabber import SponsrGrabber


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
    with tempfile.TemporaryDirectory() as temp_dir:
        downloader = Downloader(
            SponsrGrabber(
                SponsrAuth(Path(auth))
            ),
            Kinescope(
                KinescopeQuality.THE_BEST,
                Path(temp_dir)
            ),
            FFmpeg(),
            Path(dest_dir),
            concurrency=5,
        )
        asyncio.run(downloader.download(url))


if __name__ == '__main__':
    cli()
