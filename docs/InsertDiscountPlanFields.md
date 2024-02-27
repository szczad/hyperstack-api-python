# InsertDiscountPlanFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **int** |  | [optional] 
**org_name** | **str** |  | [optional] 
**discount_resources** | [**List[DiscountResourceFields]**](DiscountResourceFields.md) |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**discount_status** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.insert_discount_plan_fields import InsertDiscountPlanFields

# TODO update the JSON string below
json = "{}"
# create an instance of InsertDiscountPlanFields from a JSON string
insert_discount_plan_fields_instance = InsertDiscountPlanFields.from_json(json)
# print the JSON string representation of the object
print InsertDiscountPlanFields.to_json()

# convert the object into a dict
insert_discount_plan_fields_dict = insert_discount_plan_fields_instance.to_dict()
# create an instance of InsertDiscountPlanFields from a dict
insert_discount_plan_fields_form_dict = insert_discount_plan_fields.from_dict(insert_discount_plan_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


