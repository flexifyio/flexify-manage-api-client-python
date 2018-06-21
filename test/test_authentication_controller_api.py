# coding: utf-8

"""
    Flexify.IO User REST API

    + Generate access token via `/rest/auth` + Authorize in Swagger UI using `Bearer TOKEN` + Enjoy Flexify.IO REST API  # noqa: E501

    OpenAPI spec version: 2.4.2
    Contact: info@flexify.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flexify_api
from flexify_api.api.authentication_controller_api import AuthenticationControllerApi  # noqa: E501
from flexify_api.rest import ApiException


class TestAuthenticationControllerApi(unittest.TestCase):
    """AuthenticationControllerApi unit test stubs"""

    def setUp(self):
        self.api = flexify_api.api.authentication_controller_api.AuthenticationControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authentication_request(self):
        """Test case for authentication_request

        Generate access token for user  # noqa: E501
        """
        pass

    def test_logout(self):
        """Test case for logout

        Logout  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
