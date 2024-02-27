# CompliancePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_model** | **str** |  | 
**resource_type** | **str** |  | 
**base_value** | **int** |  | 
**variation_min** | **int** |  | 
**variation_max** | **int** |  | 
**variation_unit** | **int** |  | 

## Example

```python
from hyperstack.models.compliance_payload import CompliancePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CompliancePayload from a JSON string
compliance_payload_instance = CompliancePayload.from_json(json)
# print the JSON string representation of the object
print CompliancePayload.to_json()

# convert the object into a dict
compliance_payload_dict = compliance_payload_instance.to_dict()
# create an instance of CompliancePayload from a dict
compliance_payload_form_dict = compliance_payload.from_dict(compliance_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


