from unittest import TestCase
from fastapi.encoders import jsonable_encoder

from test import *
from main.dto.user import CreateUserDto


class TestUserAPI(TestCase):

    def test_get_users(self):
        response = client.get("/api/user/")
        print(response.text)

    def test_create_user(self):
        data = dict(email='sss', password='ddd')
        response = client.post("/api/user/", json=jsonable_encoder(data))
        print(response.text)
