# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.volume_overview_fields import VolumeOverviewFields

class TestVolumeOverviewFields(unittest.TestCase):
    """VolumeOverviewFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VolumeOverviewFields:
        """Test VolumeOverviewFields
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VolumeOverviewFields`
        """
        model = VolumeOverviewFields()
        if include_optional:
            return VolumeOverviewFields(
                count = 56,
                using = 56,
                cost_per_hour = 1.337
            )
        else:
            return VolumeOverviewFields(
        )
        """

    def testVolumeOverviewFields(self):
        """Test VolumeOverviewFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()