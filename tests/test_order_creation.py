from helpers.user_helpers import login_user, create_order
from data.data import OrderData, UserData
import allure

class TestOrderCreation:
    
    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_authorization_status_code_200(self):
        
        with allure.step("Логин пользователя"):
            login_response = login_user(UserData.EXISTING_USER)
            access_token = login_response.json().get("accessToken")
        
        with allure.step("Создание заказа с авторизацией"):
            response = create_order(OrderData.VALID_INGREDIENTS, access_token)
        
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization_status_code_200(self):
        
        with allure.step("Создание заказа без авторизации"):
            response = create_order(OrderData.VALID_INGREDIENTS)
        
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients_status_code_200(self):
        
        with allure.step("Создание заказа с ингредиентами"):
            response = create_order(OrderData.VALID_INGREDIENTS)
        
        with allure.step("Проверка статус кода"):
            assert response.status_code == 200

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients_status_code_400(self):
        
        with allure.step("Создание заказа без ингредиентов"):
            response = create_order(OrderData.EMPTY_LIST_OF_INGREDIENTS)
        
        with allure.step("Проверка статус кода"):
            assert response.status_code == 400
        
        with allure.step("Проверка сообщения об ошибке"):
            response_json = response.json()
            assert response_json["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self):
        
        with allure.step("Создание заказа с неверным хешем ингредиентов"):
            response = create_order(OrderData.INVALID_INGREDIENTS_HASH)
        
        with allure.step("Проверка статус кода"):
            assert response.status_code == 500
    
