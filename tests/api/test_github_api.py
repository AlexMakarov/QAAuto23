import pytest



@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'][4]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenco_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_emoji_exist(github_api):
    
    r = github_api.get_emoji("books")
    #assert r['message'] == 'Not Found'
    #print(f'Response is {r.text}')
    print(r)
    #assert r.status_code == 200
    #assert r.type == object
    #print(f'Type is {r.type}')
    #assert r['type'] == object


@pytest.mark.api
def test_gist_exist(github_api):
    r = github_api.get_gists("https://api.github.com/gists/9d7521b7ac75af085af3a4ca35a4b119")
    #assert r['id'] == '6808562'
    #assert r['type'] == array
    print(r)
    #print(f'Response is {r.text}')
    #assert r.status_code == 200


@pytest.mark.api
def test_get_events(github_api):
    r = github_api.get_events('event')
    print(r)