from django.test import TestCase
from django.urls import reverse
from .models import posts
# Create your tests here.
class PostTest(TestCase):
    def setUp(self):
        posts.objects.create(text = "running a test")
    def test_text_content(self):
        post = posts.objects.get(id = 1)
        expected = f'{post.text}'
        self.assertEqual(expected, 'running a test')
class HomePageViewTest(TestCase):
    def setUp(self):
        posts.objects.create(text = "running another test")
    def test_view_url_at_exist_proper_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')