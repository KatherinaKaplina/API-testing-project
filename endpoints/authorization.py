import requests
import allure


class Authorization:
    auth_url = 'http://167.172.172.115:52355/authorize'
    token = None
    response = None

    def is_token_alive(self, token):
        response = requests.get(f'{self.auth_url}/{token}')
        self.response = response
        return response.status_code == 200

    def authorization_token(self):
        if self.token is None or not self.is_token_alive(self.token):
            try:
                response = requests.post(self.auth_url, json={"name": "Kate"})
                self.response = response
                self.token = response.json().get('token')
            except requests.exceptions.RequestException as exception:
                print(f"Authorization failed: {exception}")
                self.token = None
        return self.token

    @allure.step('Check token is not empty')
    def check_token_not_empty(self):
        assert self.token is not None

    @allure.step('Check status code')
    def check_status_code(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Check token is alive')
    def check_token_is_alive(self):
        assert self.is_token_alive(self.token)
