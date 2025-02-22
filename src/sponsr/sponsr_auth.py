from dataclasses import dataclass
from pathlib import Path
from typing import Final


@dataclass
class Cookie:
    key: str
    value: str

    def as_dict(self) -> dict[str, str]:
        return {self.key: self.value}


class SponsrAuth:
    def __init__(self, session_file: Path) -> None:
        self.session_file: Final[Path] = session_file

    def cookie(self) -> Cookie:
        with self.session_file.open() as f:
            key, value = f.read().split("=", maxsplit=1)
            return Cookie(key, value)
