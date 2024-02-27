# OrganizationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**organizations** | [**OrganizationInfoModel**](OrganizationInfoModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.organization_response_model import OrganizationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationResponseModel from a JSON string
organization_response_model_instance = OrganizationResponseModel.from_json(json)
# print the JSON string representation of the object
print OrganizationResponseModel.to_json()

# convert the object into a dict
organization_response_model_dict = organization_response_model_instance.to_dict()
# create an instance of OrganizationResponseModel from a dict
organization_response_model_form_dict = organization_response_model.from_dict(organization_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


