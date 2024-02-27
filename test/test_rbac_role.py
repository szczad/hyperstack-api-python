# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.rbac_role import RBACRole

class TestRBACRole(unittest.TestCase):
    """RBACRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RBACRole:
        """Test RBACRole
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RBACRole`
        """
        model = RBACRole()
        if include_optional:
            return RBACRole(
                status = True,
                message = '',
                role = hyperstack.models.rbac_role_fields.RBACRoleFields(
                    id = 56, 
                    name = '', 
                    description = '', 
                    policies = [
                        hyperstack.models.role_policy_fields.RolePolicyFields(
                            id = 56, 
                            name = '', 
                            description = '', )
                        ], 
                    permissions = [
                        hyperstack.models.role_permission_fields.RolePermissionFields(
                            id = 56, 
                            resource = '', 
                            permission = '', )
                        ], 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return RBACRole(
        )
        """

    def testRBACRole(self):
        """Test RBACRole"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
