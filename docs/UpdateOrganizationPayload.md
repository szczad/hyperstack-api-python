# UpdateOrganizationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from hyperstack.models.update_organization_payload import UpdateOrganizationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationPayload from a JSON string
update_organization_payload_instance = UpdateOrganizationPayload.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationPayload.to_json())

# convert the object into a dict
update_organization_payload_dict = update_organization_payload_instance.to_dict()
# create an instance of UpdateOrganizationPayload from a dict
update_organization_payload_form_dict = update_organization_payload.from_dict(update_organization_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


