# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.deployment_fieldsforstartdeployments import DeploymentFieldsforstartdeployments

class TestDeploymentFieldsforstartdeployments(unittest.TestCase):
    """DeploymentFieldsforstartdeployments unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeploymentFieldsforstartdeployments:
        """Test DeploymentFieldsforstartdeployments
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeploymentFieldsforstartdeployments`
        """
        model = DeploymentFieldsforstartdeployments()
        if include_optional:
            return DeploymentFieldsforstartdeployments(
                id = 56,
                name = '',
                description = '',
                template = '',
                status = '',
                variables = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return DeploymentFieldsforstartdeployments(
        )
        """

    def testDeploymentFieldsforstartdeployments(self):
        """Test DeploymentFieldsforstartdeployments"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
