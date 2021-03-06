# coding: utf-8

"""
    Post-it digitalization API

    Post-it digitalization API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: muellerobin95@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_index_post_its(self):
        """Test case for index_post_its

        Detects Post-it notes and digitalizes their contents  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
