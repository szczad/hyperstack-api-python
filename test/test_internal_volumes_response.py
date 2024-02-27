# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.internal_volumes_response import InternalVolumesResponse

class TestInternalVolumesResponse(unittest.TestCase):
    """InternalVolumesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InternalVolumesResponse:
        """Test InternalVolumesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InternalVolumesResponse`
        """
        model = InternalVolumesResponse()
        if include_optional:
            return InternalVolumesResponse(
                status = True,
                message = '',
                volumes = [
                    hyperstack.models.internal_volume_fields.InternalVolumeFields(
                        id = 56, 
                        name = '', 
                        description = '', 
                        volume_type = '', 
                        size = '', )
                    ]
            )
        else:
            return InternalVolumesResponse(
        )
        """

    def testInternalVolumesResponse(self):
        """Test InternalVolumesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
