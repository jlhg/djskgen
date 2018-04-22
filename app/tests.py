import json

from django.test import SimpleTestCase, RequestFactory

from app.views import index


class TestView(SimpleTestCase):
    def test_main_view_returns_ok_status_on_get(self):
        request = RequestFactory().get('/')

        response = index(request)

        self.assertEqual(response.status_code, 200)

    def test_main_view_returns_ok_status_on_post(self):
        request = RequestFactory().post('/')

        response = index(request)

        self.assertEqual(response.status_code, 200)

    def test_main_view_returns_json_list_on_post(self):
        request = RequestFactory().post('/')

        response = index(request)

        secret_keys = json.loads(response.content.decode())
        self.assertIsInstance(secret_keys, list)

    def test_main_view_returns_twenty_items_on_post(self):
        request = RequestFactory().post('/')

        response = index(request)

        secret_keys = json.loads(response.content.decode())
        self.assertEqual(len(secret_keys), 20)

    def test_main_view_returns_json_list_of_dicts_on_post(self):
        request = RequestFactory().post('/')

        response = index(request)

        secret_keys = json.loads(response.content.decode())
        for secret_key in secret_keys:
            self.assertIsInstance(secret_key, str)

    def test_main_view_returns_method_not_allowed_for_put(self):
        request = RequestFactory().put('/')

        response = index(request)

        self.assertEqual(response.status_code, 405)

    def test_main_view_returns_method_not_allowed_for_delete(self):
        request = RequestFactory().delete('/')

        response = index(request)

        self.assertEqual(response.status_code, 405)
