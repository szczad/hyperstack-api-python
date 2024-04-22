# AdminOrganizationsSummaryResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**organizations** | [**List[AdminOrganizationSummaryFields]**](AdminOrganizationSummaryFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.admin_organizations_summary_response_model import AdminOrganizationsSummaryResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AdminOrganizationsSummaryResponseModel from a JSON string
admin_organizations_summary_response_model_instance = AdminOrganizationsSummaryResponseModel.from_json(json)
# print the JSON string representation of the object
print(AdminOrganizationsSummaryResponseModel.to_json())

# convert the object into a dict
admin_organizations_summary_response_model_dict = admin_organizations_summary_response_model_instance.to_dict()
# create an instance of AdminOrganizationsSummaryResponseModel from a dict
admin_organizations_summary_response_model_form_dict = admin_organizations_summary_response_model.from_dict(admin_organizations_summary_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


