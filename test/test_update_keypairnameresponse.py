# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.update_keypairnameresponse import UpdateKeypairnameresponse

class TestUpdateKeypairnameresponse(unittest.TestCase):
    """UpdateKeypairnameresponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateKeypairnameresponse:
        """Test UpdateKeypairnameresponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateKeypairnameresponse`
        """
        model = UpdateKeypairnameresponse()
        if include_optional:
            return UpdateKeypairnameresponse(
                status = True,
                message = '',
                keypair = hyperstack.models.keypair_fields.KeypairFields(
                    id = 56, 
                    name = '', 
                    environment = '', 
                    public_key = '', 
                    fingerprint = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
            )
        else:
            return UpdateKeypairnameresponse(
        )
        """

    def testUpdateKeypairnameresponse(self):
        """Test UpdateKeypairnameresponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()