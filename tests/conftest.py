from helpers.user_helpers import login_user, delete_user_by_token
import pytest
from faker import Faker
import allure


fake = Faker()

@pytest.fixture
def generate_user_data():

    user_data = {
        "email": fake.email(),
        "password": fake.password(length=8),
        "name": fake.first_name()
    }
    yield user_data
    
    with allure.step("Удаление пользователя"):
        login_response = login_user({
            "email": user_data["email"],
            "password": user_data["password"]
        })
        if login_response.status_code == 200:
            access_token = login_response.json().get("accessToken")
            delete_user_by_token(access_token)