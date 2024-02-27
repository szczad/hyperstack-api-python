# OrganizationInfoModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**users** | [**List[OrganizationUserModel]**](OrganizationUserModel.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.organization_info_model import OrganizationInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationInfoModel from a JSON string
organization_info_model_instance = OrganizationInfoModel.from_json(json)
# print the JSON string representation of the object
print OrganizationInfoModel.to_json()

# convert the object into a dict
organization_info_model_dict = organization_info_model_instance.to_dict()
# create an instance of OrganizationInfoModel from a dict
organization_info_model_form_dict = organization_info_model.from_dict(organization_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


