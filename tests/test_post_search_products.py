import requests
from utilities.configuration import get_config
from utilities.resources import ApiResource

def test_post_search_products():
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.search_product
    response = requests.post(url,data={"search_product": "tshirt"})
    body = response.json()
    print(body)
    assert response.status_code== 200
    assert "products" in body