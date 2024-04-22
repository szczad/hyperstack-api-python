# DiscountPlanFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**resource_id** | **int** |  | [optional] 
**resource_name** | **str** |  | [optional] 
**resource_count** | **int** |  | [optional] 
**discount_type** | **str** |  | [optional] 
**discount_code** | **str** |  | [optional] 
**discount_percent** | **float** |  | [optional] 
**discount_amount** | **float** |  | [optional] 
**discount_status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.discount_plan_fields import DiscountPlanFields

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountPlanFields from a JSON string
discount_plan_fields_instance = DiscountPlanFields.from_json(json)
# print the JSON string representation of the object
print(DiscountPlanFields.to_json())

# convert the object into a dict
discount_plan_fields_dict = discount_plan_fields_instance.to_dict()
# create an instance of DiscountPlanFields from a dict
discount_plan_fields_form_dict = discount_plan_fields.from_dict(discount_plan_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


