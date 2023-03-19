import dataclasses
import time
from typing import Iterable

from bs4 import BeautifulSoup

from auth import login
from config import config
from session import session
from telegram_setup import send_message


@dataclasses.dataclass
class TeslaData:
    title: str
    url: str


def run_script():
    last_title = ""
    last_link = ""

    login()

    response = session.get(config.URL.format(1), headers=config.HEADERS)

    soup = BeautifulSoup(response.content, "html.parser")

    max_pagination_number = (
        soup.find_all("nav", {"class": "pagination"})[0]
        .find_next("span", {"class": "pagination__current"})
        .text
    )

    max_pagination_number = int(max_pagination_number.split("/")[1].strip())

    for page in range(1, max_pagination_number):
        for item in _get_tesla_data_by_pagination_number(page):
            if item.title != last_title and item.url != last_link:
                send_message(item.title, item.url)
                last_title = item.title
                last_link = item.url
                time.sleep(config.INTERVAL)


def _get_tesla_data_by_pagination_number(number: int) -> Iterable[TeslaData]:
    response = session.get(config.URL.format(number), headers=config.HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = soup.find_all("blog-post-card")

    for article in articles:
        title = article.find_next("p").find("a").text
        link = article.find_next("p").find("a")["href"]
        yield TeslaData(title=title, url=link)
