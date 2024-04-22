# DiscountFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | [optional] 
**org_name** | **str** |  | [optional] 
**plan_type** | **str** |  | [optional] 
**vm_id** | **int** |  | [optional] 
**vm_name** | **str** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**discount_status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.discount_fields import DiscountFields

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountFields from a JSON string
discount_fields_instance = DiscountFields.from_json(json)
# print the JSON string representation of the object
print(DiscountFields.to_json())

# convert the object into a dict
discount_fields_dict = discount_fields_instance.to_dict()
# create an instance of DiscountFields from a dict
discount_fields_form_dict = discount_fields.from_dict(discount_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


