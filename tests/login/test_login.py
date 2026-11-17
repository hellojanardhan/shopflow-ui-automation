from config.config import ConfigManager
from utils import data_generator

config_manager = ConfigManager()

def test_login_with_valid_credentials(login_page):

    username = config_manager.USERNAME
    password = config_manager.PASSWORD
    login_page.login(username, password)


def test_login_with_invalid_username(login_page):
    username = data_generator.generate_username()
    password = config_manager.PASSWORD
    login_page.login(username, password)

def test_login_with_invalid_password(login_page):
    username = config_manager.USERNAME
    password = data_generator.generate_password()
    login_page.login(username, password)

def test_login_with_invalid_credentials(login_page):
    login_page.login("" , "")
