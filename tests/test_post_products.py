import requests
from utilities.configuration import get_config
from utilities.resources import ApiResource

def test_post_all_products():
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.products_list
    response = requests.post(url,data={})
    body = response.json()
    print(body)
    assert body["responseCode"] == 405
    assert "not supported" in body["message"]


