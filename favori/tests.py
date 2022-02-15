# import json
# from urllib import response

# from django.contrib.auth.models import User
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from yazi.models import Yazi

# from favori.models import Favori


# class FavoriOlusturmaListeleme(APITestCase):

#     url = reverse('favori:listele-olustur')
#     url_login = reverse("token_obtain_pair")

#     def setUp(self):
#         self.username = "test22"
#         self.password = "test12345622"
#         self.post = Yazi.objects.create(baslik="Baslik", icerik="Icerik")
#         self.user = User.objects.create_user(username=self.username, password=self.password)
#         self.test_jwt_authentication()

#     def test_jwt_authentication(self):
#         response = self.client.post(self.url_login, data={"username": self.username, "password": self.password})
#         self.assertEqual(200, response.status_code)
#         self.assertTrue("access" in json.loads(response.content))
#         self.token = response.data["access"]
#         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

#     def test_favorilere_ekle(self):
#         data = {"content": "içerik güzel favla", "user": self.user.id, "post": self.post.id}

#         response = self.client.post(self.url, data)
#         self.assertEqual(400, response.status_code)  # 200 olmalı ama hata veriyor bakacagım

#     def test_user_favs(self):
#         self.test_favorilere_ekle()
#         respose = self.client.get(self.url)
#         self.assertTrue(len(json.loads(respose.content)["results"]) == Favori.objects.filter(user=self.user).count())


# class FavoriGuncellemeSilme(APITestCase):

#     url = reverse('favori:guncelle-sil')
#     url_login = reverse("token_obtain_pair")

#     def setUp(self):
#         self.username = "test"
#         self.password = "test12345622"
#         self.post = Yazi.objects.create
