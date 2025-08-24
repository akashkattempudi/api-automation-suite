import requests
from utilities.configuration import get_config
from utilities.resources import ApiResource

def test_put_brands():
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.brands_list
    response = requests.put(url,data={})
    body = response.json()
    print(body)
    assert body["responseCode"] == 405
    assert "not supported" in body["message"]