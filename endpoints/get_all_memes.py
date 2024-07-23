from test_api_final_kkaplina.endpoints.endpoint import Endpoint
import requests
import allure
from requests.exceptions import JSONDecodeError


class GetAllMemes(Endpoint):
    @allure.step('get all memes')
    def get_all_memes(self, token, headers=None):
        headers = headers if headers else self.get_headers(token)
        self.response = requests.get(
            f'{self.url}',
            headers=headers
        )
        if self.response.status_code == 200:
            try:
                self.json = self.response.json()
            except JSONDecodeError:
                self.json = None
        else:
            self.json = None

    @allure.step('Check response is list')
    def check_response_is_list(self, data):
        assert self.json is not None and isinstance(data, list)
