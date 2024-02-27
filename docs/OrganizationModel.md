# OrganizationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**organization** | [**OrganizationInfoModel**](OrganizationInfoModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.organization_model import OrganizationModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationModel from a JSON string
organization_model_instance = OrganizationModel.from_json(json)
# print the JSON string representation of the object
print OrganizationModel.to_json()

# convert the object into a dict
organization_model_dict = organization_model_instance.to_dict()
# create an instance of OrganizationModel from a dict
organization_model_form_dict = organization_model.from_dict(organization_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


