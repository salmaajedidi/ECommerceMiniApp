from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    def setUp(self):
        
        self.client = APIClient()
        self.product_data = {
            'nom': 'Product 1',
            'description': 'Description of Product 1',
            'prix': 100.0,
            'stock': 10
        }
        self.product = Product.objects.create(**self.product_data)
        self.url = '/api/products/'  

    def test_get_products(self): 
        # Fetch the list of products
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

    def test_post_product(self):
        new_product_data = {
            'nom': 'Product 2',
            'description': 'Description of Product 2',
            'prix': 150.0,
            'stock': 20
        }
        response = self.client.post(self.url, new_product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nom'], 'Product 2')

    def test_post_invalid_product(self):

        invalid_data = {
            'nom': '',  # Invalid data (empty 'nom')
            'prix': 150.0,
            'stock': 20
        }
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
