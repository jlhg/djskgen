from unittest import mock

from django.test import SimpleTestCase, RequestFactory
from django.conf import settings

from app.views import IndexView, SecretKeyView


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
    def test_that_it_returns_secret_key_in_response(self):
        request = RequestFactory().post('/')

        response = SecretKeyView().list(request)

        self.assertIn('secret_key', response.data)

    def test_that_it_returns_a_secret_key_with_fifty_characters(self):
        request = RequestFactory().post('/')

        response = SecretKeyView().list(request)

        self.assertEqual(len(response.data['secret_key']), 50)

    def test_that_it_returns_a_secret_key_as_string(self):
        request = RequestFactory().post('/')

        response = SecretKeyView().list(request)

        self.assertIsInstance(response.data['secret_key'], str)
