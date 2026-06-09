import requests
from data.data import Urls



def post_create_user(user_data):
    url = f"{Urls.BASE_URL}{Urls.CREATE_USER}"
    response = requests.post(url, json=user_data)
    return response

def post_login_user(login_data):

    url = f"{Urls.BASE_URL}{Urls.LOGIN_USER}"
    response = requests.post(url, json=login_data)
    return response

def post_create_order(order_data, access_token=None):
    url = f"{Urls.BASE_URL}{Urls.CREATE_ORDER}"
    headers = {}
    
    if access_token:
        headers["Authorization"] = access_token
    
    response = requests.post(url, json=order_data, headers=headers)
    return response


def delete_user(access_token):
    url = f"{Urls.BASE_URL}{Urls.DEL_USER}"
    headers = {"Authorization": access_token}
    return requests.delete(url, headers=headers)