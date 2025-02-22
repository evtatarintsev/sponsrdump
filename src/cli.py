import click


@click.group("dump")
def cli():
    ...


@cli.command()
@click.option("--url", "-url", required=True, help='URL видео на sponsr.ru.')
@click.option('--dest-dir', "-d", help="Директория для загрузки файла")
def video(url: str, dest: str):
    """Сохраняет видео по указанному url в директорию dest."""
    ...


if __name__ == '__main__':
    cli()
