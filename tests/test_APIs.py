import pytest
import allure
from .test_data import (TEST_DATA_CREATE, NEGATIVE_DATA_CREATE, NEGATIVE_DATA_UPDATE, TEST_DATA_UPDATE,
                        invalid_token, another_user_token)


@allure.title('Create new meme')
@pytest.mark.parametrize('data', TEST_DATA_CREATE)
def test_add_meme(post_create_meme, data, token):
    post_create_meme.new_meme(data, token)
    post_create_meme.check_status_code_is_correct(status_code=200)
    post_create_meme.check_text_is_correct(data['text'])
    post_create_meme.check_url_is_correct(data['url'])
    post_create_meme.check_tags_is_correct(data['tags'])
    post_create_meme.check_info_is_correct(data['info'])


@allure.title('Create new meme - unauthorized user')
def test_add_meme_unauthorized(post_create_meme):
    post_create_meme.new_meme(TEST_DATA_CREATE[0], invalid_token)
    post_create_meme.report_errors()
    post_create_meme.check_status_code_is_unauthorized(status_code=401)


@allure.title('Create new meme - negative checks')
@pytest.mark.parametrize('data', NEGATIVE_DATA_CREATE)
def test_add_meme_with_negative_data(post_create_meme, data, token):
    post_create_meme.new_meme(data, token)
    post_create_meme.check_status_code_is_bad_request(status_code=400)


@allure.title('Update meme')
def test_update_meme(new_meme_id, put_update_meme, token):
    data = TEST_DATA_UPDATE
    data["id"] = new_meme_id
    put_update_meme.make_changes_in_meme(new_meme_id, data, token)
    put_update_meme.check_status_code_is_correct(status_code=200)
    put_update_meme.check_text_is_correct(data['text'])
    put_update_meme.check_url_is_correct(data['url'])
    put_update_meme.check_tags_is_correct(data['tags'])
    put_update_meme.check_info_is_correct(data['info'])


@allure.title('Update meme - unauthorized user')
def test_update_meme_unauthorized(put_update_meme):
    meme_id = 100
    put_update_meme.make_changes_in_meme(meme_id, TEST_DATA_CREATE[0], invalid_token)
    put_update_meme.report_errors()
    put_update_meme.check_status_code_is_unauthorized(status_code=401)


@allure.title('Update meme - forbidden for another user')
def test_update_meme_forbidden(put_update_meme):
    meme_id = 100
    put_update_meme.make_changes_in_meme(meme_id, TEST_DATA_CREATE[0], another_user_token)
    put_update_meme.report_errors()
    put_update_meme.check_status_code_is_forbidden(status_code=403)


@allure.title('Update meme - negative checks')
@pytest.mark.parametrize('data', NEGATIVE_DATA_UPDATE)
def test_update_meme_with_negative_data(put_update_meme, new_meme_id, data, token):
    put_update_meme.make_changes_in_meme(new_meme_id, data, token)
    put_update_meme.check_status_code_is_bad_request(status_code=400)


@allure.title('Get one meme')
def test_get_one_meme(new_meme_id, get_request_meme, token):
    response = get_request_meme.get_meme_by_id(new_meme_id, token)
    if response is not None:
        get_request_meme.check_status_code_is_correct(status_code=200)
        get_request_meme.check_id_is_correct(response['id'])
        get_request_meme.check_text_is_correct(response['text'])
        get_request_meme.check_url_is_correct(response['url'])
        get_request_meme.check_tags_is_correct(response['tags'])
        get_request_meme.check_info_is_correct(response['info'])


@allure.title('Get one meme - unauthorized user')
def test_get_one_meme_unauthorized(get_request_meme):
    meme_id = 100
    get_request_meme.get_meme_by_id(meme_id, invalid_token)
    get_request_meme.report_errors()
    get_request_meme.check_status_code_is_unauthorized(status_code=401)


@allure.title('Get all memes')
def test_get_all_meme(get_request_all_memes, token):
    response = get_request_all_memes.get_all_memes(token)
    if response is not None:
        get_request_all_memes.check_status_code_is_correct(status_code=200)
        data_list = response.get('data', [])
        get_request_all_memes.check_response_is_list(data_list)
        for meme in data_list:
            get_request_all_memes.check_id_not_empty(meme)
            get_request_all_memes.check_text_not_empty(meme)
            get_request_all_memes.check_url_not_empty(meme)
            get_request_all_memes.check_tags_not_empty(meme)
            get_request_all_memes.check_info_not_empty(meme)


@allure.title('Get all memes - unauthorized user')
def test_get_all_meme_unauthorized(get_request_all_memes):
    get_request_all_memes.get_all_memes(invalid_token)
    get_request_all_memes.report_errors()
    get_request_all_memes.check_status_code_is_unauthorized(status_code=401)


@allure.title('Delete meme')
def test_delete_meme(new_meme_id, delete_meme, token):
    delete_meme.delete_meme_by_id(new_meme_id, token)
    delete_meme.check_status_code_is_correct(status_code=200)


@allure.title('Delete meme - unauthorized user')
def test_delete_meme_unauthorized(delete_meme):
    meme_id = 100
    delete_meme.delete_meme_by_id(meme_id, invalid_token)
    delete_meme.report_errors()
    delete_meme.check_status_code_is_unauthorized(status_code=401)


@allure.title('Delete meme - forbidden for another user')
def test_delete_meme_forbidden(delete_meme):
    meme_id = 100
    delete_meme.delete_meme_by_id(meme_id, another_user_token)
    delete_meme.report_errors()
    delete_meme.check_status_code_is_forbidden(status_code=403)
