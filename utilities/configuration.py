import json
import random
import configparser
def get_config():
    config = configparser.ConfigParser()
    config.read('C:\\Users\\akash\\PycharmProjects\\api_project\\properties.ini')
    return config
def login_data():
    path = "C:\\Users\\akash\\PycharmProjects\\api_project\\utilities\\login_data.json"
    with open(path,"r") as f:
        return json.load(f)
def register_data():
    path = "C:\\Users\\akash\\PycharmProjects\\api_project\\utilities\\register_data.json"
    with open(path,"r") as f:
        data =  json.load(f)
        random_user = random.choice(data["users"])
        return random_user

