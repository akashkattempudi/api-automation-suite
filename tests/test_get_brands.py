import requests
from utilities.configuration import get_config
from utilities.resources import ApiResource
def test_get_all_brands():
    config = get_config()
    url = config['API']['endpoint'] + ApiResource.brands_list
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 200
    assert "brands" in response.json()
