from sqlite3 import apilevel
from django.test import TestCase,Client

from rest_framework.test import APIRequestFactory

from .models import category, manufacturer, product
# Create your tests here.


class TestProducts(TestCase):

    """
    Things to test

    -can product model create values?
    -Are they linked correctly?
    -Are the foreignkeys proper?
    
    """

    def setUp(self):
        self.category = category.objects.create(
            name = "Entertainment",
            catDesc = "For all your movie, music and party"
        )

        self.manufacturer = manufacturer.objects.create(
            name = "Alphabet",
            manDesc = "Do The Right Thing"
       )

        self.product = product.objects.create(
            title = "Studio",
            proDesc = "Cloud at your hands",
            price = 180000,
            cat = self.category,
            man = self.manufacturer,
            rating = 7 
        )

    def test_instance(self):
        #Proper value
        self.assertEqual(self.product.title, "Studio")
        self.assertEqual(self.product.price, 180000)
        self.assertEqual(self.product.cat.name, "Entertainment")
        self.assertEqual(self.product.man.name, "Alphabet")

    def test_cat_intance(self):
        self.assertEqual(self.category.name, "Entertainment")
        self.assertEqual(self.product.cat.name, "Entertainment")

    def test_man_instance(self):
        self.assertEqual(self.manufacturer.name, self.product.man.name)



class TestProductViews(TestCase):
    
    """
    Things to test
    
    - Can we create a product listing?
    - Edited?
    - Listed?
    - Deleted?
    """

    def test_category_create(self):
        """Test - Create Category"""

        item = {"id": 1, "name": "Business", "catDesc": "For the Executive Look"}
        factory = APIRequestFactory()
        request = factory.post('/products/category', data=item, format='json')

    def test_manufacturer_create(self):
        """Test - Create manufacturer"""

        item = {"id": 1, "name": "Apple", "manDesc": "Think Different!"}
        factory = APIRequestFactory()
        request = factory.post('/products/manufacturer', data=item, format='json')

    def test_product_create(self):
        """Test - Creating product"""

        item = {"id":1, "title": "iphone", "proDesc": "Expensive", "price": 100000, "cat": 1, "man": 1, "rating": 8} 
        # response = Client.post('/products/product', data=item, content_type="application/json")
        # print(response)
        # self.assertEqual(response.status_code, 201)
        factory = APIRequestFactory()
        request = factory.post('/products/product', data=item, format='json')

    def test_product_get(self):
        """Test - Listing product"""

        factory = APIRequestFactory()
        request = factory.get('/products/product')

    def test_product_put(self):
        """Test - Editing product"""

        factory = APIRequestFactory()
        request = factory.put('/products/product/1/', {"proDesc": "Think Different — But Not Too Different"}, format='json')

    def test_product_delete(self):
        """Test - Deleting product"""

        factory = APIRequestFactory()
        request = factory.delete('/products/product/1/')