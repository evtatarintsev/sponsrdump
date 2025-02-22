from pathlib import Path


class FFmpeg:
    def concat(self, video: Path, audio: Path, dest: Path) -> None:
        """Объединяет потоки из видео и аудио фалов в один."""