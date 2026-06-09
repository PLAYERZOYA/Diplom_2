#эндпоинты, данные пользователя (json записанные в переменные), ингредиенты какие есть

class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru'
    
    CREATE_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    CREATE_ORDER = '/api/orders'
    GET_INGREDIENTS = '/api/ingredients'
    DEL_USER = '/api/auth/user'


class UserData:
  
    EXISTING_USER = {
        "email": "existing_user@yandex.ru",
        "password": "existing123",
        "name": "AlreadyExist"
    }
    
    USER_WITHOUT_EMAIL = {
        "email": "",
        "password": "password123",
        "name": "NoEmail"
    }
    
    USER_WITHOUT_PASSWORD = {
        "email": "withoutpassword@yandex.ru",
        "password": "",
        "name": "NoPassword"
    }
    
    USER_WITHOUT_NAME = {
        "email": "noname@yandex.ru",
        "password": "NoName",
        "name": ""
    }

    INVALID_LOGIN_DATA = {
        "email": "wrong@yandex.ru",
        "password": "wrongpassword"
    }



fluorescent_bun = "61c0c5a71d1f82001bdaaa6d"
crator_bun = '61c0c5a71d1f82001bdaaa6c'

sauce_spicy_x = "61c0c5a71d1f82001bdaaa72"
space_sauce = "61c0c5a71d1f82001bdaaa73"
traditional_galactic_sauce = "61c0c5a71d1f82001bdaaa74"
sauce_with_spikes = "61c0c5a71d1f82001bdaaa75"

immortal_shellfish_meat = "61c0c5a71d1f82001bdaaa6f"
beef_meteorite = "61c0c5a71d1f82001bdaaa70"
bio_cutlet = "61c0c5a71d1f82001bdaaa71"
fillet = "61c0c5a71d1f82001bdaaa6e"
crispy_rings = "61c0c5a71d1f82001bdaaa76"
fruits_of_tree = "61c0c5a71d1f82001bdaaa77"
crystals = "61c0c5a71d1f82001bdaaa78"
mini_salad = "61c0c5a71d1f82001bdaaa79"
cheeze = "61c0c5a71d1f82001bdaaa7a"



class OrderData:

    VALID_INGREDIENTS = {
        "ingredients": [
            crator_bun,
            sauce_spicy_x,
            cheeze
        ]
    }

    

    EMPTY_LIST_OF_INGREDIENTS = {
        "ingredients": []
    }
    

    INVALID_INGREDIENTS_HASH = {
        "ingredients": ["12345w", "678910g"]
    }
    

