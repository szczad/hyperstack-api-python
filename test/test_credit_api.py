# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.api.credit_api import CreditApi


class TestCreditApi(unittest.TestCase):
    """CreditApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CreditApi()

    def tearDown(self) -> None:
        pass

    def test_check_balance_as_an_organization(self) -> None:
        """Test case for check_balance_as_an_organization

        GET: View credit and threshold
        """
        pass


if __name__ == '__main__':
    unittest.main()
