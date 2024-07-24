import allure
from .test_data import invalid_token


@allure.title('Check authorization - get valid token')
def test_get_token(auth):
    auth.authorization_token()
    auth.check_token_not_empty()
    auth.check_status_code(status_code=200)


@allure.title('Check authorization - token is alive')
def test_is_token_alive(auth):
    auth.authorization_token()
    auth.check_token_is_alive()
    auth.check_status_code(status_code=200)


@allure.title('Check authorization - refresh token')
def test_refresh_token(auth):
    auth.token = invalid_token
    auth.authorization_token()
    auth.check_token_not_empty()
    auth.check_token_is_alive()
    auth.check_status_code(status_code=200)
