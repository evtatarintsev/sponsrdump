from sponsr.sponsr_auth import SponsrAuth
from sponsr.sponsr_post import SponsrPost


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
        self.auth = auth

    def post(self, url: str) -> SponsrPost:
        return SponsrPost("")
