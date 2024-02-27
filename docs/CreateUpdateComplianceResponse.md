# CreateUpdateComplianceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**compliance** | [**ComplianceModelFields**](ComplianceModelFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.create_update_compliance_response import CreateUpdateComplianceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpdateComplianceResponse from a JSON string
create_update_compliance_response_instance = CreateUpdateComplianceResponse.from_json(json)
# print the JSON string representation of the object
print CreateUpdateComplianceResponse.to_json()

# convert the object into a dict
create_update_compliance_response_dict = create_update_compliance_response_instance.to_dict()
# create an instance of CreateUpdateComplianceResponse from a dict
create_update_compliance_response_form_dict = create_update_compliance_response.from_dict(create_update_compliance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


