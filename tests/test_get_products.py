import requests
from utilities.configuration import get_config
from utilities.resources import ApiResource

def test_get_all_products():
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.products_list
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 200
    assert "products" in response.json()

