from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.food = Image(name = 'food', description = 'food character')
        self.food.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.food, Image))


    def test_save_method(self):
        self.food.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 


    def test_delete_method(self):
        self.new_image = Image(name = 'food', description = 'the beauty of a foods despite its thorns')  
        self.new_image.save_image() 
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)


    def test_update_method(self):
        self.vic = Image(name = 'epic', description = 'an image of Epic')
        self.vic.save_image()
        self.vic = Image(name = 'epic', description = 'an image of Epic')        
        self.vic.update_image(name = 'epic')
        self.vic.save_image()
        images = Image.objects.filter(name = 'epic')
        pics = Image.objects.all()      
        self.assertEqual(len(images), 1)




class CategoryTestClass(TestCase):
    def setUp(self):
        self.travel = Category(name = 'Travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.travel, Category))

    def test_save_method(self):
        self.travel.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)        

    def test_delete_method(self):
        self.new_category = Category(name = 'Food')
        self.new_category.save_category()
        self.new_category.delete_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)   

    def test_update_category(self):
        self.health = Category(name = 'Food')
        self.health.save_category()
        self.health = Category(name = 'Fashion')
        self.health.save_category()
        self.health.update_category(name = 'Travel')
        categories = Category.objects.filter(name = 'People')
        self.assertEqual(len(categories), 1)




class LocationTestClass(TestCase):    
    def setUp(self):
        self.Rwanda = Location(name = ' Rwanda')

    def test_instance(self):
        self.assertTrue(isinstance(self.Rwanda, Location))

    def test_save_method(self):
        self.Rwanda.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.new_location = Location(name = 'Rubavu')
        self.new_location.save_location()
        self.new_location.delete_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations), 0)

    def test_update_method(self):
        self.Kigali = Location(name = 'Rubavu')
        self.Kigali.save_location()
        self.Kigali = Location(name = 'Kigali')
        self.Kigali.save_location()
        self.Kigali.update_location(name = 'Kigali')
        locations = Location.objects.filter(name = 'Kigali')
        self.assertEqual(len(locations), 1)   