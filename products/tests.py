from django.test import TestCase

from .models import category, manufacturer, product
# Create your tests here.


class TestExample(TestCase):

    """
    Things to test

    -is product listing proper?
    -can user create a listing?
    -can user edit a listing?
    -is the redirection proper?
    -can user delete a listing?
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
