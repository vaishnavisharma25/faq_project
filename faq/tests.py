from django.urls import reverse
from rest_framework.test import APITestCase
from .models import FAQ

class FAQTests(APITestCase):
    def setUp(self):
        FAQ.objects.create(question="What is Django?", answer="A web framework.")

    def test_faq_translation(self):
        response = self.client.get(reverse('faq-list') + '?lang=hi')
        self.assertEqual(response.status_code, 200)
        self.assertIn('translated_question', response.data[0])

    def test_fallback_to_english(self):
        response = self.client.get(reverse('faq-list') + '?lang=fr')
        self.assertEqual(response.data[0]['translated_question'], "What is Django?")