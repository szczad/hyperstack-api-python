# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.payment_details_fields import PaymentDetailsFields

class TestPaymentDetailsFields(unittest.TestCase):
    """PaymentDetailsFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentDetailsFields:
        """Test PaymentDetailsFields
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentDetailsFields`
        """
        model = PaymentDetailsFields()
        if include_optional:
            return PaymentDetailsFields(
                amount = 1.337,
                currency = '',
                paid_from = '',
                status = '',
                gateway_response = '',
                description = '',
                transaction_id = '',
                payment_id = '',
                updated_at = ''
            )
        else:
            return PaymentDetailsFields(
        )
        """

    def testPaymentDetailsFields(self):
        """Test PaymentDetailsFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
