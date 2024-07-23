import allure
from .authorization import Authorization


class Endpoint:
    url = 'http://167.172.172.115:52355/meme'
    # auth_url = 'http://167.172.172.115:52355/authorize'
    response = None
    json = None
    errors = []
    auth = Authorization()

    def get_headers(self, token=None):
        if token is None:
            token = self.auth.authorization_token()
        return {
            'Content-Type': 'application/json',
            'Authorization': f'{token}'
        }

    def log_response(self):
        if self.response:
            allure.attach(str(self.response.status_code), 'Status Code')
            allure.attach(self.response.text, 'Response Body')

    @allure.step('Check status code')
    def check_status_code_is_correct(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Check that 400 error received')
    def check_status_code_is_bad_request(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Check text')
    def check_text_is_correct(self, text):
        assert self.json is not None and self.json['text'] == text

    @allure.step('Check url')
    def check_url_is_correct(self, url):
        assert self.json is not None and self.json['url'] == url

    @allure.step('Check tags')
    def check_tags_is_correct(self, tags):
        assert self.json is not None and self.json['tags'] == tags

    @allure.step('Check info')
    def check_info_is_correct(self, info):
        assert self.json is not None and self.json['info'] == info

    @allure.step('Check id')
    def check_id_is_correct(self, meme_id):
        assert self.json is not None and self.json['id'] == meme_id

    @allure.step('Check id is not empty')
    def check_id_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        id_meme = meme.get('id', '')
        if not id:
            self.errors.append(f"Id field is empty in meme: {id_meme}")

    @allure.step('Check text is not empty')
    def check_text_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        text = meme.get('text', '')
        if not text:
            self.errors.append(f"Text field is empty in meme: {meme}")

    @allure.step('Check url is not empty')
    def check_url_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        url = meme.get('url', '')
        if not url:
            self.errors.append(f"URL field is empty in meme: {meme}")

    @allure.step('Check tags is not empty')
    def check_tags_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        tags = meme.get('tags', '')
        if not tags:
            self.errors.append(f"Tags field is empty in meme: {meme}")

    @allure.step('Check info is not empty')
    def check_info_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        info = meme.get('info', '')
        if not info:
            self.errors.append(f"Info field is empty in meme: {meme}")

    @allure.step('Report errors')
    def report_errors(self):
        if self.errors:
            error_report = '\n'.join(self.errors)
            raise AssertionError(f"Test failed with the following errors:\n{error_report}")

    @allure.step('Check 401 error')
    def check_status_code_is_unauthorized(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Check 403 error')
    def check_status_code_is_forbidden(self, status_code):
        assert self.response.status_code == status_code
