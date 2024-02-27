# OrganizationObjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | [optional] 
**resources** | [**List[InfrahubResourceObjectResponse]**](InfrahubResourceObjectResponse.md) |  | [optional] 

## Example

```python
from hyperstack.models.organization_object_response import OrganizationObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationObjectResponse from a JSON string
organization_object_response_instance = OrganizationObjectResponse.from_json(json)
# print the JSON string representation of the object
print OrganizationObjectResponse.to_json()

# convert the object into a dict
organization_object_response_dict = organization_object_response_instance.to_dict()
# create an instance of OrganizationObjectResponse from a dict
organization_object_response_form_dict = organization_object_response.from_dict(organization_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


