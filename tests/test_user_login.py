from helpers.user_helpers import login_user
from data.data import UserData
import allure


class TestUserLogin:
    
    @allure.title('Вход под существующим пользователем')
    def test_login_existing_user_status_code_200(self):

        login_data = {
            "email": UserData.EXISTING_USER["email"],
            "password": UserData.EXISTING_USER["password"]
        }
        
        response = login_user(login_data)
        
        assert response.status_code == 200
        


    @allure.title("Вход с неверным логином и паролем")
    def test_login_with_invalid_login_and_password_401_status_code(self):

        response = login_user(UserData.INVALID_LOGIN_DATA)
        
        assert response.status_code == 401
        
        response_json = response.json()
        assert response_json["message"] == "email or password are incorrect"