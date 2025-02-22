from __future__ import annotations

from dataclasses import dataclass, fields
from typing import Any

import httpx

from sponsr.sponsr_auth import SponsrAuth
from sponsr.sponsr_post import SponsrPostPreview
from sponsr.sponsr_project import SponsrProjectPage


@dataclass
class SponsrPostsApiPost:
    post_id: int
    post_text: str
    post_title: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> SponsrPostsApiPost:
        field_names = {f.name for f in fields(SponsrPostsApiPost)}
        filtered_data = {k: v for k, v in data.items() if k in field_names}
        return SponsrPostsApiPost(**filtered_data)


class SponsrGrabber:
    headers: dict[str, str] = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ru,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    def __init__(self, auth: SponsrAuth) -> None:
        self.cookie = auth.cookie()

    async def posts(self, url: str) -> list[SponsrPostPreview]:
        async with httpx.AsyncClient(headers=self.headers, cookies=self.cookie.as_dict()) as client:
            response = await client.get(url)
            project_id = SponsrProjectPage(response.text).project_id()

        posts: list[SponsrPostsApiPost] = []
        total_posts = 1

        async with httpx.AsyncClient(headers=self.headers, cookies=self.cookie.as_dict()) as client:
            while len(posts) < total_posts:
                response = await client.get(f"https://sponsr.ru/project/{project_id}/more-posts/?offset={len(posts)}")
                data = response.json()["response"]
                total_posts = data["rows_count"]
                posts += [SponsrPostsApiPost.from_dict(d) for d in data["rows"]]

        return [SponsrPostPreview(post.post_title, post.post_text) for post in reversed(posts)]
