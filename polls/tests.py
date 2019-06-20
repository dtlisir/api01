# -*- coding: utf-8 -*-
# author: dtlisir
# date: 2019/6/20
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from polls import apiviews

class PollTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 300,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

