import os
from dotenv import load_dotenv

load_dotenv()


class ConfigManager:

    BASE_URL = os.getenv("BASE_URL")
    SAUCEDEMO_USERNAME = os.getenv("SAUCEDEMO_USERNAME")
    SAUCEDEMO_PASSWORD = os.getenv("SAUCEDEMO_PASSWORD")
    LOCKED_USER = os.getenv("LOCKED_USER")
