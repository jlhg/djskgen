from django.test import SimpleTestCase, RequestFactory

from app.views import IndexView, SecretKeysView


class TestIndexView(SimpleTestCase):
    def test_main_view_returns_ok_status_on_get(self):
        request = RequestFactory().get('/')

        response = IndexView(request=request).get(request)

        self.assertEqual(response.status_code, 200)


class TestSecretKeysView(SimpleTestCase):
    def test_main_view_returns_json_list_on_post(self):
        request = RequestFactory().post('/')

        response = SecretKeysView().list(request)

        self.assertIsInstance(response.data, list)

    def test_main_view_returns_twenty_items_on_post(self):
        request = RequestFactory().post('/')

        response = SecretKeysView().list(request)

        self.assertEqual(len(response.data), 20)

    def test_main_view_returns_json_list_of_strings_on_post(self):
        request = RequestFactory().post('/')

        response = SecretKeysView().list(request)

        for secret_key in response.data:
            self.assertIsInstance(secret_key, str)
