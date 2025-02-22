from typing import Final
from bs4 import BeautifulSoup

class SponsrProjectPage:
    def __init__(self, html: str) -> None:
        self.html: Final[str] = html

    def project_id(self) -> int:
        soup = BeautifulSoup(self.html, "lxml")
        tags = soup.find_all(id='project_id')
        if not tags:
            raise Exception("tag with project_id not found on project page")
        return int(tags[0]['value'])