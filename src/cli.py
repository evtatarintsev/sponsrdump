import asyncio
from pathlib import Path

import click

from sponsr.sponsr_auth import SponsrAuth
from sponsr.sponsr_grabber import SponsrGrabber
from sponsr.sponsr_post import SponsrPost


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
    asyncio.run(save_video(url, dest_dir, auth))


async def save_video(url: str, dest_dir: str, auth: str) -> None:
    """Сохраняет видео по указанному url в директорию dest."""
    post = await SponsrGrabber(
        SponsrAuth(Path(auth))
    ).post(url)
    click.echo(post.html)


if __name__ == '__main__':
    cli()
