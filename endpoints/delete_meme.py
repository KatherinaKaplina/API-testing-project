import requests
import allure
from test_api_final_kkaplina.endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    @allure.step('delete meme')
    def delete_meme_by_id(self, meme_id, token, headers=None):
        # print(f"Deleting meme with id: {meme_id}")
        headers = headers if headers else self.get_headers(token)
        self.response = requests.delete(f'{self.url}/{meme_id}', headers=headers)
        return self.response
