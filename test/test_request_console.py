# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.request_console import RequestConsole

class TestRequestConsole(unittest.TestCase):
    """RequestConsole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestConsole:
        """Test RequestConsole
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestConsole`
        """
        model = RequestConsole()
        if include_optional:
            return RequestConsole(
                status = True,
                message = '',
                url = ''
            )
        else:
            return RequestConsole(
        )
        """

    def testRequestConsole(self):
        """Test RequestConsole"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()