from django.test import TestCase
from cart.models import Category, Product

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="shirts")

    def test_category_name_is_correct(self):
        """category name is correct"""
        shirts = Category.objects.get(name="shirts")
        self.assertEqual(shirts.name, 'shirts')

class ProductTestCase(TestCase):
    def setUp(self):
        shirts = Category.objects.create(name="shirts")
        Product.objects.create(title="green shirt", 
        description = "a shirt that is green",
        primary_category = shirts)

    def test_product_attributes_are_correct(self):
        """test product attributes are correct"""
        shirt = Product.objects.get(title="green shirt")
        self.assertEqual(shirt.title, "green shirt")
        self.assertEqual(shirt.description, "a shirt that is green")
        self.assertEqual(shirt.primary_category.name, "shirts")
        
        
