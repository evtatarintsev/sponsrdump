from typing import Final
from urllib.parse import parse_qs, urlparse

from bs4 import BeautifulSoup


class SponsrPostPreview:
    def __init__(self, title: str, html: str) -> None:
        self.title: Final[str] = title
        self.html: Final[str] = html

    def kinescope(self) -> list[str]:
        soup = BeautifulSoup(self.html)
        mpds = []
        iframes_src = [f["src"] for f in soup.find_all("iframe")]
        video_src = [ src for src in iframes_src if "video" in src]

        for src in video_src:
            file_id = parse_qs(urlparse(src).query).get('video_id')
            if file_id:
                # workaround bogus links like /post/video/?video_id=xxx?poster_id=yyy
                file_id = file_id[0].partition('?')[0]
                mpds.append(f"https://kinescope.io/{file_id}/master.mpd")
        return mpds
