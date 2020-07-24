# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.post_it import PostIt  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_index_post_its(self):
        """Test case for index_post_its

        Detects Post-it notes and digitalizes their contents
        """
        body = Object()
        query_string = [('picture_link', 'picture_link_example')]
        response = self.client.open(
            '/RobinTTYTeam/AppliedAI/1.0.0/indexPostIts',
            method='POST',
            data=json.dumps(body),
            content_type='image/png',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
