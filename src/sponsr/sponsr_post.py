from typing import Final


class SponsrPost:
    def __init__(self, html: str) -> None:
        self.html: Final[str] = html
