# OrganizationsResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**organizations** | [**List[OrganizationInfoModel]**](OrganizationInfoModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.organizations_response_model import OrganizationsResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsResponseModel from a JSON string
organizations_response_model_instance = OrganizationsResponseModel.from_json(json)
# print the JSON string representation of the object
print OrganizationsResponseModel.to_json()

# convert the object into a dict
organizations_response_model_dict = organizations_response_model_instance.to_dict()
# create an instance of OrganizationsResponseModel from a dict
organizations_response_model_form_dict = organizations_response_model.from_dict(organizations_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


