from pathlib import Path

import click

from sponsr.sponsr_post import SponsrPost


@click.group("dump")
def cli() -> None:
    ...


@cli.command()
@click.option("--url", "-url", required=True, help='URL видео на sponsr.ru.')
@click.option('--dest-dir', "-d",
              type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True),
              help="Директория для загрузки файла")
def video(url: str, dest_dir: str) -> None:
    """Сохраняет видео по указанному url в директорию dest."""
    SponsrPost(url)


if __name__ == '__main__':
    cli()
