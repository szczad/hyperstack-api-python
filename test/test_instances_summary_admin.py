# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.instances_summary_admin import InstancesSummaryAdmin

class TestInstancesSummaryAdmin(unittest.TestCase):
    """InstancesSummaryAdmin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstancesSummaryAdmin:
        """Test InstancesSummaryAdmin
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstancesSummaryAdmin`
        """
        model = InstancesSummaryAdmin()
        if include_optional:
            return InstancesSummaryAdmin(
                status = True,
                message = '',
                instances = [
                    hyperstack.models.instances_summary_fields.InstancesSummaryFields(
                        id = 56, 
                        name = '', 
                        environment = '', 
                        org_id = 56, 
                        environment_id = 56, 
                        image = '', 
                        image_id = 56, 
                        flavor = '', 
                        flavor_id = 56, 
                        keypair = '', 
                        keypair_id = 56, 
                        fixed_ip = '', 
                        floating_ip = '', 
                        floating_ip_status = '', 
                        status = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return InstancesSummaryAdmin(
        )
        """

    def testInstancesSummaryAdmin(self):
        """Test InstancesSummaryAdmin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()