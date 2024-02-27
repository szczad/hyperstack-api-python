# CreateDiscountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**discount_plan** | [**InsertDiscountPlanFields**](InsertDiscountPlanFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.create_discount_response import CreateDiscountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDiscountResponse from a JSON string
create_discount_response_instance = CreateDiscountResponse.from_json(json)
# print the JSON string representation of the object
print CreateDiscountResponse.to_json()

# convert the object into a dict
create_discount_response_dict = create_discount_response_instance.to_dict()
# create an instance of CreateDiscountResponse from a dict
create_discount_response_form_dict = create_discount_response.from_dict(create_discount_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


