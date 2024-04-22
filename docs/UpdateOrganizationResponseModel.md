# UpdateOrganizationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.update_organization_response_model import UpdateOrganizationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationResponseModel from a JSON string
update_organization_response_model_instance = UpdateOrganizationResponseModel.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationResponseModel.to_json())

# convert the object into a dict
update_organization_response_model_dict = update_organization_response_model_instance.to_dict()
# create an instance of UpdateOrganizationResponseModel from a dict
update_organization_response_model_form_dict = update_organization_response_model.from_dict(update_organization_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


