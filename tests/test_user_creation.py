import pytest
from helpers.user_helpers import create_user
from data.data import UserData
import allure


class TestUserCreation:
    
    @allure.title('Создание уникального пользователя')
    def test_create_unique_user_status_code_200(self, generate_user_data):
   
        response = create_user(generate_user_data)
        
        assert response.status_code == 200
        
    
    @allure.title('Создание уже существующего пользователя')
    def test_create_existing_user_response_403(self):

        response = create_user(UserData.EXISTING_USER)
        
        assert response.status_code == 403
        
        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == "User already exists"


    @allure.title('Создание пользователя с незаполненным обязательным полем')
    @pytest.mark.parametrize("invalid_user", [
        UserData.USER_WITHOUT_EMAIL,
        UserData.USER_WITHOUT_PASSWORD,
        UserData.USER_WITHOUT_NAME
    ])
    def test_create_user_missing_required_field_response_403(self, invalid_user):

        response = create_user(invalid_user)
        
        assert response.status_code == 403
        
        response_json = response.json()
        assert response_json["success"] is False
        assert response_json["message"] == "Email, password and name are required fields"