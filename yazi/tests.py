import json
from urllib import response

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from yazi.models import Yazi


class YaziListelemeOlusturmaTest(APITestCase):
    url_list = reverse("yazi:listele")
    url_create = reverse("yazi:olustur")
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "test"
        self.password = "test123456"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.test_jwt_authentication()

    def test_jwt_authentication(self):
        response = self.client.post(self.url_login, data={"username": self.username, "password": self.password})
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in json.loads(response.content))
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_yeni_yazi_ekleme(self):
        data = {"baslik": "Test Yazi", "icerik": "Test Icerik"}
        response = self.client.post(self.url_create, data)
        self.assertEqual(201, response.status_code)

    def test_giris_yapmamis_kullanici(self):
        self.client.credentials()
        data = {"baslik": "Test Yazi", "icerik": "Test Icerik"}
        response = self.client.post(self.url_create, data)
        self.assertEqual(401, response.status_code)

    def test_yazi_listeleme(self):
        response = self.client.get(self.url_list)
        self.assertEqual(200, response.status_code)
        self.assertTrue(len(json.loads(response.content)) > 0)


class YaziGuncellemeSilme(APITestCase):
    login_url = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "test"
        self.password = "test123456"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.user2 = User.objects.create_user(username="test2", password="test123456")
        self.yazi = Yazi.objects.create(baslik="Baslik", icerik="Icerik")
        self.url = reverse("yazi:guncelle", kwargs={"slug": self.yazi.slug})
        self.test_jwt_token_authentication()

    def test_jwt_token_authentication(self):
        response = self.client.post(self.login_url, data={"username": self.username, "password": self.password})
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in json.loads(response.content))
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    # silme islemi
    def test_yazi_silme(self):
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)

    def test_farkli_kullanici_yazi_silme(self):
        self.test_jwt_token_authentication(self.user2)
        response = self.client.delete(self.url)
        self.assertEqual(403, response.status_code)
