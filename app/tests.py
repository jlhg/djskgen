from django.test import SimpleTestCase, RequestFactory

from app.views import index


class TestView(SimpleTestCase):
    def test_main_view_returns_ok_status_on_get(self):
        request = RequestFactory().get('/')

        response = index(request)

        self.assertEqual(response.status_code, 200)

    def test_main_view_returns_no_codes_on_get(self):
        request = RequestFactory().get('/')

        response = index(request)

        self.assertNotIn('table', response.content)

    def test_main_view_returns_ok_status_on_post(self):
        request = RequestFactory().post('/')

        response = index(request)

        self.assertEqual(response.status_code, 200)

    def test_main_view_returns_codes_on_post(self):
        request = RequestFactory().post('/')

        response = index(request)

        self.assertIn('table', response.content)
