from django.test import TestCase
from rest_framework.test import APIClient
from .models import News_Table

class NewsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        News_Table.objects.create(News_Title="Test News 1", News_Content="This is test content 1", News_Tags="tech", News_Source="Source A")
        News_Table.objects.create(News_Title="Test News 2", News_Content="This is test content 2", News_Tags="sports", News_Source="Source B")

    def test_News_List(self):
        response = self.client.get('/api/News_Page/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        
    def test_Filter_Tags(self):
        response = self.client.get('/api/News_Page/?News_Tags=tech')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['News_Title'], "Test News 1")
    
    def test_Filter_Keywords(self):
        response = self.client.get('/api/News_Page/?keywords=This')
        self.assertEqual(len(response.data), 2)
        self.assertIn(response.data[1]["News_Source"], ["Source A", "Source B"])
    
    def test_Filter_Nonexist(self):
        response = self.client.get('/api/News_Page/?nonexist=content 1')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["News_Title"], "Test News 2")

    def test_Filter_Keywords_and_Nonexist(self):
        response = self.client.get("/api/News_Page/?keywords=content 1&nonexist=content 2")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["News_Title"], "Test News 1")