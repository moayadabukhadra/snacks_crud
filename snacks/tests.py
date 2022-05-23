
from django.test import TestCase
from .admin import AdminSnack
from django.test import TestCase
from django.urls import reverse
from .models import Snack
from django.contrib.auth.models import User
from django.test.client import Client


class SnackTest(TestCase):
    


    


    @classmethod
    def setUpTestData(cls):
        password = 'mypassword' 
        my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)
        c = Client()
        c.login(username=my_admin.username, password=password)
        snack=Snack.objects.create(id=6,name="admin",purchaser=my_admin, description="snack")
        snack.save()
    
    def test_detail_template(self):
        url = reverse("snack_list")
        response =self.client.get(url+"/5")
        self.assertEqual(response.status_code, 200)

    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response =self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_list_page_template(self):
        url = reverse("snack_list")
        response =self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")
    
    def test_create_page_status_code(self):
        url = reverse("create_snack")
        response =self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_delete_status_code(self):
    #     url = reverse("snack_list")
    #     response =self.client.get(reverse("update_snack.get_absolute_url()"))
    #     self.assertEqual(response.status_code, 200)

    # def test_logged_user_get_details(self):
    #     response = self.client.get(
    #     self.assertEqual(response.status_code, 200)
    #     response = self.client.get()
    #     self.assertEqual(response.status_code, 200)


    
