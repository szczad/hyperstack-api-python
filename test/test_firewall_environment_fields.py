# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.firewall_environment_fields import FirewallEnvironmentFields

class TestFirewallEnvironmentFields(unittest.TestCase):
    """FirewallEnvironmentFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FirewallEnvironmentFields:
        """Test FirewallEnvironmentFields
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FirewallEnvironmentFields`
        """
        model = FirewallEnvironmentFields()
        if include_optional:
            return FirewallEnvironmentFields(
                id = 56,
                name = '',
                region = ''
            )
        else:
            return FirewallEnvironmentFields(
        )
        """

    def testFirewallEnvironmentFields(self):
        """Test FirewallEnvironmentFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()