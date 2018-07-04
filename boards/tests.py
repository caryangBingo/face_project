from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.


class HomeTest(TestCase):
    """docstring for HomeTest"""

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
