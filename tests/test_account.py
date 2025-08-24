import time
import pytest
import requests
from utilities.configuration import get_config, register_data
from utilities.resources import ApiResource
@pytest.fixture(scope="module")
def user_data():
    data = register_data()
    data["email"] = f"placeholder{int(time.time())}@example.com"
    password = data["password"]
    return {"email": data["email"], "password": password, "data": data}
def test_post_create_account(user_data):
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.create_account
    response = requests.post(url,data=user_data["data"])
    body = response.json()
    print(body)
    assert body["responseCode"]== 201
    assert "User created!" in body["message"]
def test_get_user_detail(user_data):
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.get_user_detail
    response = requests.get(url, params={'email':user_data["email"]})
    body = response.json()
    print(body)
    assert response.status_code == 200
    assert body["responseCode"] == 200
    assert user_data["email"] == body["user"]["email"]
def test_put_update_account(user_data):
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.update_account
    response = requests.put(url,data=user_data['data'])
    body = response.json()
    print(body)
    assert response.status_code == 200
    assert body["responseCode"]== 200
    assert "User updated!" in body["message"]
def test_delete_account(user_data):
    data = {"email":user_data['email'],"password":user_data['password']}
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.delete_account
    response = requests.delete(url,data=data)
    body = response.json()
    print(body)
    assert response.status_code == 200
    assert body["responseCode"] == 200
    assert "Account deleted!" in body["message"]