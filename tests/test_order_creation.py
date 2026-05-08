from helpers.user_helpers import login_user, create_order
from data.data import OrderData, UserData
import allure

class TestOrderCreation:
    
    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_authorization_status_code_200(self):

        login_response = login_user(UserData.EXISTING_USER)
        access_token = login_response.json().get("accessToken")
        
        response = create_order(OrderData.VALID_INGREDIENTS, access_token)
        
        assert response.status_code == 200


    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization_status_code_200(self):

        response = create_order(OrderData.VALID_INGREDIENTS)
        
        assert response.status_code == 200
        

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients_status_code_200(self):

        response = create_order(OrderData.VALID_INGREDIENTS)
        
        assert response.status_code == 200
        

    

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients_status_code_400(self):

        response = create_order(OrderData.EMPTY_LIST_OF_INGREDIENTS)
        
        assert response.status_code == 400
        
        response_json = response.json()
        assert response_json["message"] == "Ingredient ids must be provided"
    

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self):

        response = create_order(OrderData.INVALID_INGREDIENTS_HASH)
        
        assert response.status_code == 500
        
    
