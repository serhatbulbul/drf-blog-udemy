import json
from urllib import response

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

# doğru veriler ile kayıt işlemi yap
# sifre invalid olabilir
# kullanıcı adı zaten var
# üye girisi yaptıysak o sayfa gozukmemeli
# token ile giris yapılırsa 403 hatasi


class UserKayitTestCase(APITestCase):
    url = reverse('account:register')
    url_token_login = reverse("token_obtain_pair")

    def test_kullanici_kayit(self):
        # dogru veriler ile kayit islemi

        data = {"username": "test", "password": "test123456"}
        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

    def test_invalid_sifre_ile_kayit(self):
        # invalid sifre ile kayit

        data = {"username": "test", "password": "1"}
        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_benzersiz_isim_ile_kayit(self):
        # benzersiz isim ile kayit
        self.test_kullanici_kayit()

        data = {"username": "test", "password": "test123456"}
        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_giris_yapildiysa_kayit_sayfasini_goremez(self):
        # giris yapildiysa 403

        self.test_kullanici_kayit()  # yeni kayit olusturmayi calıstır
        self.client.login(username='test', password='test123456')  # olusan kayit ile giris yap
        response = self.client.post(self.url)  # kayit sayfasina yeniden giris yapmaya calıstır
        self.assertEqual(403, response.status_code)

    def test_token_ile_kullanici_girisi(self):
        # token ile giris yapılırsa 403 hatasi

        self.test_kullanici_kayit()  # yeni kayit olusturmayi calıstır
        data = {"username": "test", "password": "test123456"}  # giris yapılacak veriler

        response = self.client.post(self.url_token_login, data)  # yeni yapilan kayit ile token icin giris yaptık
        self.assertEqual(200, response.status_code)  # yeni kayit ile girisin dorulugunu kontrol ediyoruz
        token = response.data['access']  # token alıyoruz
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)  # aldigimiz token ile giris yapıyoruz

        response_2 = self.client.post(self.url)  # uye kayit sayfasına istekte bulunuzyoruz
        self.assertEqual(403, response_2.status_code)  # token ile giris yaptıgımız icin 403 hatasi alıyoruz


class KullaniciGirisTestCase(APITestCase):
    url_token_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "test"
        self.password = "test123456"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_kullanici_token_giris(self):
        # dogru veriler ile giris yapma
        data = {"username": self.username, "password": self.password}
        response = self.client.post(self.url_token_login, data)
        self.assertEqual(200, response.status_code)
        # print(json.loads(response.content))
        self.assertTrue('access' in json.loads(response.content))

    def test_kullanici_invalid_data(self):
        response = self.client.post(self.url_token_login, {"username": "qqqqqqqq", "password": "qwwqwqwwqqw22121"})
        self.assertEqual(401, response.status_code)

    def test_kullanici_bos_data(self):
        response = self.client.post(self.url_token_login, {"username": "", "password": ""})
        self.assertEqual(400, response.status_code)
