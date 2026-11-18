from config.config import ConfigManager
from utils.data_generator import generate_username, generate_password
from utils.logger import get_logger

config_manager = ConfigManager()
logger = get_logger("LoginTests")


def test_login_with_valid_credentials(login_page):

    logger.info("Test started: Login with valid credentials")

    username = config_manager.SAUCEDEMO_USERNAME
    password = config_manager.SAUCEDEMO_PASSWORD

    login_page.login(username, password)

    logger.info("Test completed: Login with valid credentials")

def test_login_with_invalid_username(login_page):

    logger.info("Test started: Login with invalid username")

    username = generate_username()
    password = config_manager.SAUCEDEMO_PASSWORD

    login_page.login(
        username,
        password,
        "Epic sadface: Username and password do not match any user in this service",
    )

    logger.info("Test completed: Login with invalid username")

def test_login_with_invalid_password(login_page):

    logger.info("Test started: Login with invalid password")

    username = config_manager.SAUCEDEMO_USERNAME
    password = generate_password()

    login_page.login(
        username,
        password,
        "Epic sadface: Username and password do not match any user in this service",
    )

    logger.info("Test completed: Login with invalid password")


def test_login_with_invalid_credentials(login_page):

    logger.info("Test started: Login with invalid credentials")

    username = generate_username()
    password = generate_password()

    login_page.login(
        username,
        password,
        "Epic sadface: Username and password do not match any user in this service",
    )

    logger.info("Test completed: Login with invalid credentials")


def test_login_with_both_fields_empty(login_page):

    logger.info("Test started: Login with both fields empty")

    login_page.login("", "", "Epic sadface: Username is required")

    logger.info("Test completed: Login with both fields empty")


def test_login_with_empty_username_and_valid_password(login_page):

    logger.info("Test started: Login with empty username")

    password = config_manager.SAUCEDEMO_PASSWORD

    login_page.login("", password, "Epic sadface: Username is required")

    logger.info("Test completed: Login with empty username")


def test_login_with_valid_username_and_empty_password(login_page):

    logger.info("Test started: Login with empty password")

    username = config_manager.SAUCEDEMO_USERNAME

    login_page.login(username, "", "Epic sadface: Password is required")

    logger.info("Test completed: Login with empty password")


def test_login_with_locked_out_user(login_page):

    logger.info("Test started: Login with locked-out user")

    username = config_manager.LOCKED_USER
    password = config_manager.SAUCEDEMO_PASSWORD

    login_page.login(
        username,
        password,
        "Epic sadface: Sorry, this user has been locked out.",
    )

    logger.info("Test completed: Login with locked-out user")


def test_login_using_enter_key(login_page):

    logger.info("Test started: Login using Enter key")

    username = config_manager.SAUCEDEMO_USERNAME
    password = config_manager.SAUCEDEMO_PASSWORD

    login_page.login_using_enter_key(username, password)

    logger.info("Test completed: Login using Enter key")


def test_password_field_is_masked(login_page):

    logger.info("Test started: Verify password field masking")

    assert login_page.is_password_masked(), "Password field should be masked by default"

    logger.info("Test passed: Password field is masked")


def test_dismiss_login_error_message(login_page):

    logger.info("Test started: Dismiss login error message")

    username = generate_username()
    password = generate_password()

    login_page.dismiss_login_error_message(username, password)

    logger.info("Test completed: Dismiss login error message")
