from test_api_final_kkaplina.endpoints.endpoint import Endpoint
import requests
import allure
from requests.exceptions import JSONDecodeError


class GetMeme(Endpoint):
    @allure.step('get meme by id')
    def get_meme_by_id(self, new_meme_id, token, headers=None):
        headers = headers if headers else self.get_headers(token)
        self.response = requests.get(
            f'{self.url}/{new_meme_id}',
            headers=headers
        )
        if self.response.status_code == 200:
            try:
                self.json = self.response.json()
            except JSONDecodeError:
                self.json = None
        else:
            self.json = None
