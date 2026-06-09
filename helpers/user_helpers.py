

from data.data import UserData
from helpers.api_requests import post_create_user, post_login_user, post_create_order, delete_user



def create_user(user_data):

    response = post_create_user(user_data)
    return response

def login_user(login_data):
    response = post_login_user(login_data)
    return response


def create_order(order_data, access_token=None):

    response = post_create_order(order_data, access_token)
    return response

def get_user_token():
    response = login_user(UserData.EXISTING_USER)
    if response.status_code == 200:
        return response.json().get("accessToken")
    return None

def delete_user_by_token(access_token):

    response = delete_user(access_token)
    return response