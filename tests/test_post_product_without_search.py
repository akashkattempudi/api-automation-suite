import requests
from utilities.configuration import get_config
from utilities.resources import ApiResource

def test_post_product_without_search():
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.search_product
    response = requests.post(url,data={})
    body = response.json()
    print(body)
    assert body["responseCode"]== 400
    assert "Bad request" in body["message"]