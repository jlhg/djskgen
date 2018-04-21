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

        self.assertNotIn('</ul>', response.content.decode())

    def test_main_view_returns_ok_status_on_post(self):
        request = RequestFactory().post('/')

        response = index(request)

        self.assertEqual(response.status_code, 200)

    def test_main_view_returns_codes_on_post(self):
        request = RequestFactory().post('/')

        response = index(request)

        self.assertIn('</ul>', response.content.decode())

    def test_main_view_returns_method_not_allowed_for_put(self):
        request = RequestFactory().put('/')

        response = index(request)

        self.assertEqual(response.status_code, 405)

    def test_main_view_returns_method_not_allowed_for_delete(self):
        request = RequestFactory().delete('/')

        response = index(request)

        self.assertEqual(response.status_code, 405)
