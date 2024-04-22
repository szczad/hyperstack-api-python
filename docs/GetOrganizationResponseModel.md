# GetOrganizationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**organization** | [**OrganizationFields**](OrganizationFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.get_organization_response_model import GetOrganizationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationResponseModel from a JSON string
get_organization_response_model_instance = GetOrganizationResponseModel.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationResponseModel.to_json())

# convert the object into a dict
get_organization_response_model_dict = get_organization_response_model_instance.to_dict()
# create an instance of GetOrganizationResponseModel from a dict
get_organization_response_model_form_dict = get_organization_response_model.from_dict(get_organization_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


