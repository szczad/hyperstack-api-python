# ComplianceFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpu_model** | **str** |  | [optional] 
**cpu** | **List[int]** |  | [optional] 
**ram** | **List[int]** |  | [optional] 
**hdd** | **List[int]** |  | [optional] 

## Example

```python
from hyperstack.models.compliance_fields import ComplianceFields

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceFields from a JSON string
compliance_fields_instance = ComplianceFields.from_json(json)
# print the JSON string representation of the object
print(ComplianceFields.to_json())

# convert the object into a dict
compliance_fields_dict = compliance_fields_instance.to_dict()
# create an instance of ComplianceFields from a dict
compliance_fields_form_dict = compliance_fields.from_dict(compliance_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


