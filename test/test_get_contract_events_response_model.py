# coding: utf-8

"""
    Infrahub-API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from hyperstack.models.get_contract_events_response_model import GetContractEventsResponseModel

class TestGetContractEventsResponseModel(unittest.TestCase):
    """GetContractEventsResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetContractEventsResponseModel:
        """Test GetContractEventsResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetContractEventsResponseModel`
        """
        model = GetContractEventsResponseModel()
        if include_optional:
            return GetContractEventsResponseModel(
                status = True,
                message = '',
                contract_events = [
                    hyperstack.models.admin_contract_event_fields.AdminContractEventFields(
                        id = 56, 
                        user_id = 56, 
                        org_id = 56, 
                        time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        type = '', 
                        reason = '', 
                        message = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                count = 56
            )
        else:
            return GetContractEventsResponseModel(
        )
        """

    def testGetContractEventsResponseModel(self):
        """Test GetContractEventsResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()