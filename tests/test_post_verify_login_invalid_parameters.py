import requests
from utilities.configuration import get_config
from utilities.resources import ApiResource
from utilities.configuration import login_data
def test_post_verify_login_invalid_email_parameters():
    data = login_data()["valid_user"]["email"]
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.verify_login
    response = requests.post(url,data={"email":data})
    body = response.json()
    print(body)
    assert body["responseCode"] == 400
    assert "Bad request" in body["message"]

def test_post_verify_login_invalid_password_parameters():
    data = login_data()["valid_user"]["password"]
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.verify_login
    response = requests.post(url,data={'password':data})
    body = response.json()
    print(body)
    assert body["responseCode"] == 400
    assert "Bad request" in body["message"]