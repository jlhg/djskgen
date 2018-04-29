from unittest import mock

from django.test import SimpleTestCase, RequestFactory
from django.conf import settings

from app.views import IndexView, SecretKeysView


class TestIndexView(SimpleTestCase):
    def test_that_it_returns_ok_status_on_get(self):
        request = RequestFactory().get('/')

        response = IndexView(request=request).get(request)

        self.assertEqual(response.status_code, 200)

    def test_when_analytics_is_set_then_render_with_analytics(self):
        ga_id = 'google-analytics-id'
        request = RequestFactory().get('/')

        with mock.patch.object(settings, 'GOOGLE_ANALYTICS_ID', ga_id):
            response = IndexView(request=request).get(request)

        response.render()
        self.assertIn(ga_id, response.rendered_content)

    def test_when_analytics_is_set_and_query_param_disables_it_then_render_without_analytics(self):
        ga_id = 'google-analytics-id'
        request = RequestFactory().get('/', {'analytics': '0'})

        with mock.patch.object(settings, 'GOOGLE_ANALYTICS_ID', ga_id):
            response = IndexView(request=request).get(request)

        response.render()
        self.assertNotIn(ga_id, response.rendered_content)


class TestSecretKeysView(SimpleTestCase):
    def test_that_it_returns_json_list_on_post(self):
        request = RequestFactory().post('/')

        response = SecretKeysView().list(request)

        self.assertIsInstance(response.data, list)

    def test_that_it_returns_twenty_items_on_post(self):
        request = RequestFactory().post('/')

        response = SecretKeysView().list(request)

        self.assertEqual(len(response.data), 20)

    def test_that_it_returns_json_list_of_strings_on_post(self):
        request = RequestFactory().post('/')

        response = SecretKeysView().list(request)

        for secret_key in response.data:
            self.assertIsInstance(secret_key, str)
