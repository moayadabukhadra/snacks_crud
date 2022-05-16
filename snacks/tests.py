
from django.test import TestCase
from .admin import AdminSnack
from urllib import request, response
from django.test import TestCase
from django.urls import reverse
from .models import Snack

class SnackTest(TestCase):

    
    def test_detail_template(self):
        url = reverse("snack_detail",kwargs={'pk':3})
        response =self.client.get(url)
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

    
