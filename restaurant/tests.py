from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Restaurant

class RestaurantViewTest(TestCase):
    def setUp(self):
        User = get_user_model()  # Use get_user_model() to get the custom user model
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a sample restaurant for testing
        self.restaurant = Restaurant.objects.create(
            name='Sample Restaurant',
            location='Sample Location',
            address='123 Sample St, Sample City, SS 12345',
            rating=4.5
        )

    def test_create_restaurant(self):
        response = self.client.post('/restaurants/create/', {
            'name': 'New Restaurant',
            'location': 'New Location',
            'address': '456 New St, New City, NC 45678',
            'rating': 5.0
        })
        self.assertEqual(response.status_code, 302)  # Assuming a redirect on success
        self.assertTrue(Restaurant.objects.filter(name='New Restaurant').exists())

    def test_restaurant_detail_view(self):
        response = self.client.get(f'/restaurants/{self.restaurant.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.restaurant.name)

    def test_restaurant_list_view(self):
        response = self.client.get('/restaurants/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.restaurant.name)