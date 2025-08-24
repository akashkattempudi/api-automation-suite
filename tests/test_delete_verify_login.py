import requests
from utilities.configuration import get_config
from utilities.resources import ApiResource

def test_delete_verify_login():
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.verify_login
    response = requests.delete(url,data={"email":"akashkattempudi002@gmail.com","password":"23145r67tuygjhnv"})
    body = response.json()
    print(body)
    assert body["responseCode"]== 405
    assert "This request method is not supported." in body["message"]