# OrganizationResourceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**organization** | [**OrganizationResources**](OrganizationResources.md) |  | [optional] 

## Example

```python
from hyperstack.models.organization_resource_response import OrganizationResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationResourceResponse from a JSON string
organization_resource_response_instance = OrganizationResourceResponse.from_json(json)
# print the JSON string representation of the object
print OrganizationResourceResponse.to_json()

# convert the object into a dict
organization_resource_response_dict = organization_resource_response_instance.to_dict()
# create an instance of OrganizationResourceResponse from a dict
organization_resource_response_form_dict = organization_resource_response.from_dict(organization_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


