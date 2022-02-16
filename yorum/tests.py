# import json

# from django.contrib.auth.models import User
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from yazi.models import Yazi

# from yorum.models import Yorum


# class YorumGuncellemeSilmeTest(APITestCase):
#     login_url = reverse('token_obtain_pair')

#     def setUp(self):
#         self.username = "test"
#         self.password = "test123456"
#         self.yazi = Yazi.objects.create(baslik="Baslik", icerik="Icerik")
#         self.user = User.objects.create_user(username=self.username, password=self.password)
#         self.user2 = User.objects.create_user(username="test2", password="test123456")
#         self.yorum = Yorum.objects.create(yazi=self.yazi, ana_yorum="ana_yorum", user=self.user, post=self.yazi)
#         self.url = reverse("yorum:guncelle", kwargs={"pk": self.yorum.pk})
#         self.test_jwt_token_authenication()

#         def test_jwt_token_authenication(self, username="test", password="test123456"):
#             response = self.client.post(self.login_url, data={"username": username, "password": password})
#             self.assertEqual(response.status_code, 200)
#             self.assertTrue("access" in json.loads(response.content))
#             self.token = response.data['access']
#             self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

#     # # # # yorum silme islemi testi

#     # # # def test_yorum_silme(self):
#     # # #     response = self.client.delete(self.urls)
#     # # #     self.assertEqual(response.status_code, 204)
#     # # #     self.assertFalse(Yorum.objects.filter(pk=self.ana_yorum.pk).exists())

#     # # # # kendimizin olmayan bir degeri silmek
#     # # # def test_baskasinin_yorumu_silme(self):
#     # # #     self.test_jwt_token_authenication("test2")
#     # # #     response = self.client.delete(self.url)
#     # # #     self.assertEqual(response.status_code, 403)
#     # # #     self.assertTrue(Yorum.objects.get(pk=self.ana_yorum.pk))
