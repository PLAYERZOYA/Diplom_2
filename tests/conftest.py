import pytest
from faker import Faker

fake = Faker()


@pytest.fixture
def generate_user_data():

    user_data = {
        "email": fake.email(),
        "password": fake.password(length=8),
        "name": fake.first_name()
    }
    return user_data