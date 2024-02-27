# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.organization_object_response import OrganizationObjectResponse

class TestOrganizationObjectResponse(unittest.TestCase):
    """OrganizationObjectResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationObjectResponse:
        """Test OrganizationObjectResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationObjectResponse`
        """
        model = OrganizationObjectResponse()
        if include_optional:
            return OrganizationObjectResponse(
                org_id = 56,
                resources = [
                    hyperstack.models.infrahub_resource_object_response.InfrahubResourceObjectResponse(
                        type = '', 
                        name = '', 
                        infrahub_id = 56, 
                        status = '', 
                        host = '', 
                        price = 1.337, 
                        actual_price = 1.337, 
                        host_price = 1.337, 
                        actual_host_price = 1.337, 
                        nexgen_price = 1.337, 
                        nexgen_actual_price = 1.337, )
                    ]
            )
        else:
            return OrganizationObjectResponse(
        )
        """

    def testOrganizationObjectResponse(self):
        """Test OrganizationObjectResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
