from test_api_final_kkaplina.endpoints.endpoint import Endpoint
from requests.exceptions import JSONDecodeError
import requests
import allure


class UpdateMeme(Endpoint):
    @allure.step('update meme')
    def make_changes_in_meme(self, meme_id, payload, token, headers=None):
        headers = headers if headers else self.get_headers(token)
        self.response = requests.put(
            f'{self.url}/{meme_id}',
            json=payload,
            headers=headers
        )
        try:
            self.json = self.response.json()
        except JSONDecodeError:
            self.json = None
        return self.response
