from pathlib import Path

import click


@click.group("dump")
def cli():
    ...


@cli.command()
@click.option("--url", "-url", required=True, help='URL видео на sponsr.ru.')
@click.option('--dest-dir', "-d",
              type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True),
              help="Директория для загрузки файла")
def video(url: str, dest_dir: str):
    """Сохраняет видео по указанному url в директорию dest."""
    ...


if __name__ == '__main__':
    cli()
