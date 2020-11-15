from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class LocationTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.test_location = Location(location="kitchen")


class CategoryTestClass(TestCase):
    def setUp(self):
        self.test = Category(category="food")

    

    



