# ComplianceModelFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**gpu_model** | **str** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**base_value** | **int** |  | [optional] 
**variation_min** | **int** |  | [optional] 
**variation_max** | **int** |  | [optional] 
**variation_unit** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.compliance_model_fields import ComplianceModelFields

# TODO update the JSON string below
json = "{}"
# create an instance of ComplianceModelFields from a JSON string
compliance_model_fields_instance = ComplianceModelFields.from_json(json)
# print the JSON string representation of the object
print ComplianceModelFields.to_json()

# convert the object into a dict
compliance_model_fields_dict = compliance_model_fields_instance.to_dict()
# create an instance of ComplianceModelFields from a dict
compliance_model_fields_form_dict = compliance_model_fields.from_dict(compliance_model_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


