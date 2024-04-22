# CreateContarctFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**org_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**expiration_policy** | **int** |  | [optional] 
**discount_plans** | [**List[DiscountPlanFields]**](DiscountPlanFields.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.create_contarct_fields import CreateContarctFields

# TODO update the JSON string below
json = "{}"
# create an instance of CreateContarctFields from a JSON string
create_contarct_fields_instance = CreateContarctFields.from_json(json)
# print the JSON string representation of the object
print(CreateContarctFields.to_json())

# convert the object into a dict
create_contarct_fields_dict = create_contarct_fields_instance.to_dict()
# create an instance of CreateContarctFields from a dict
create_contarct_fields_form_dict = create_contarct_fields.from_dict(create_contarct_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


