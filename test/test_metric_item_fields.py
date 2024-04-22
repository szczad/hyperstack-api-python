# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.metric_item_fields import MetricItemFields

class TestMetricItemFields(unittest.TestCase):
    """MetricItemFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetricItemFields:
        """Test MetricItemFields
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetricItemFields`
        """
        model = MetricItemFields()
        if include_optional:
            return MetricItemFields(
                unit = '',
                columns = ["time","granularity","value"],
                data = [["2023-09-01T01:19:00+00:00",60,1041433070000000],["2023-09-01T01:24:00+00:00",60,1041441320000000]]
            )
        else:
            return MetricItemFields(
        )
        """

    def testMetricItemFields(self):
        """Test MetricItemFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()