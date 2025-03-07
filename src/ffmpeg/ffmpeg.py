from pathlib import Path
from subprocess import Popen, PIPE


class FFmpeg:
    def concat(self, video: Path, audio: Path, dest: Path) -> None:
        """Объединяет потоки из видео и аудио файлов в один."""
        cmd = [
            "ffmpeg",
            "-y", # перезаписывать файл, если он существует, чтобы не подвисала команда в ожидании пользователя
            "-i", str(video.absolute()),
            "-i", str(audio.absolute()),
            "-c", "copy",
            str(dest.absolute())
        ]
        prc = Popen(cmd, stdout=PIPE, stderr=PIPE)

        out, err = [item.decode() if item else '' for item in prc.communicate()]

        if prc.wait():
            raise Exception(f'Command error:\n{cmd}\n\n{out}\n\n{err}\n----------')
