from typing import Final, TypeAlias
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup


class SponsrPostPreview:
    def __init__(self, id: int, title: str, html: str) -> None:
        self.id = id
        self.title: Final[str] = title
        self.html: Final[str] = html

    def video_ids(self) -> list[str]:
        soup = BeautifulSoup(self.html, "lxml")
        mpds = []
        iframes_src = [f["src"] for f in soup.find_all("iframe")]
        video_src = [src for src in iframes_src if "video" in src]

        for src in video_src:
            query_file_id = parse_qs(urlparse(src).query).get('video_id')
            if query_file_id:
                # workaround bogus links like /post/video/?video_id=xxx?poster_id=yyy
                file_id = query_file_id[0].partition('?')[0]
                mpds.append(file_id)
        return mpds
