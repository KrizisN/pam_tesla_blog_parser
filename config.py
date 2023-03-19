import os

from utils import Singleton


class Config(metaclass=Singleton):
    def __init__(self):
        self.URL = "https://www.tesmanian.com/blogs/tesmanian-blog?page={}"

        self.INTERVAL = 15

        self.BOT_TOKEN = os.environ.get(
            "BOT_TOKEN", "6025845945:AAF9d-k4111-88La26zwLr4yYR8agBHznh8"
        )
        self.CHAT_ID = os.environ.get(
            "CHAT_ID"
        )  # You can check your chat id using userinfobot in telegram

        self.ACC_EMAIL = os.environ.get("ACC_EMAIL")
        self.ACC_PASSWORD = os.environ.get("ACC_PASSWORD")

        self.HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }


config = Config()
