import os
from dotenv import load_dotenv

load_dotenv()


class ConfigManager:

    BASE_URL = os.getenv("BASE_URL")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
