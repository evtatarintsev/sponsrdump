from typing import Final


class SponsrPostPreview:
    def __init__(self, title: str, html: str) -> None:
        self.title: Final[str] = title
        self.html: Final[str] = html
