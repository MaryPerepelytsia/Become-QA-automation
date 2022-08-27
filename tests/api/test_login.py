import requests

def test_http_status_code200():
    r = requests.get('https://api.github.com/zen')
    #print(r.__dict__)
    assert r.status_code == 200
    assert r.text != "Half measures are as bad as nothing at all."

def test_user():
    r = requests.get('https://api.github.com/users/defunkt')
    #print(r.__dict__)
    assert r.json()['login'] == 'defunkt'
    assert r.json()['id'] == 2


def test_user_non_exists():
    r = requests.get('https://api.github.com/users/abrahggjgfkgfkg')
    #print(r.__dict__)
    assert r.status_code == 404
    assert r.json()['message'] == 'Not Found'
      