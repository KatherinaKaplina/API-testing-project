import pytest
# from test_api_final_kkaplina.endpoints.endpoint import Endpoint
from test_api_final_kkaplina.endpoints.create_meme import CreateMeme
from test_api_final_kkaplina.endpoints.update_meme import UpdateMeme
from test_api_final_kkaplina.endpoints.get_meme import GetMeme
from test_api_final_kkaplina.endpoints.get_all_memes import GetAllMemes
from test_api_final_kkaplina.endpoints.delete_meme import DeleteMeme
from test_api_final_kkaplina.endpoints.authorization import Authorization


@pytest.fixture(scope='session')
def auth():
    return Authorization()


@pytest.fixture(scope='session')
def token(auth):
    return auth.authorization_token()


@pytest.fixture()
def post_create_meme():
    return CreateMeme()


@pytest.fixture()
def put_update_meme():
    return UpdateMeme()


@pytest.fixture()
def get_request_meme():
    return GetMeme()


@pytest.fixture()
def get_request_all_memes():
    return GetAllMemes()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()


@pytest.fixture()
def new_meme_id(post_create_meme, delete_meme, token):
    payload = {
        "text": "Relax, it's not a competition",
        "url": "https://i.pinimg.com/474x/95/7d/ee/957dee125eeec88b8c4b2ba493d13182.jpg",
        "tags": ["squirrel_1", "squirrel_2", "squirrel_3"],
        "info": {"squirrel": ["healthy", "sporty"]}
    }
    response = post_create_meme.new_meme(payload, token)
    meme_id = response.json()['id']
    yield meme_id
    delete_meme.delete_meme_by_id(f'{meme_id}', token)
