import requests
from utilities.configuration import get_config
from utilities.resources import ApiResource
from utilities.configuration import login_data
def test_post_verify_login():
    data = login_data()["valid_user"]
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.verify_login
    response = requests.post(url,data=data)
    body = response.json()
    print(body)
    assert response.status_code== 200
    assert "User exists!" in body["message"]