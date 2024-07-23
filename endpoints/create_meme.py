import requests
import allure
from requests.exceptions import JSONDecodeError
from test_api_final_kkaplina.endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    @allure.step('create new meme')
    def new_meme(self, payload, token, headers=None):
        headers = headers if headers else self.get_headers(token)
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        try:
            self.json = self.response.json()
        except JSONDecodeError:
            self.json = None
        return self.response
