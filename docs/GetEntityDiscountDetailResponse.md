# GetEntityDiscountDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**organization** | [**List[DiscountPlanFields]**](DiscountPlanFields.md) |  | [optional] 
**virtual_machine** | [**List[DiscountPlanFields]**](DiscountPlanFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.get_entity_discount_detail_response import GetEntityDiscountDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetEntityDiscountDetailResponse from a JSON string
get_entity_discount_detail_response_instance = GetEntityDiscountDetailResponse.from_json(json)
# print the JSON string representation of the object
print(GetEntityDiscountDetailResponse.to_json())

# convert the object into a dict
get_entity_discount_detail_response_dict = get_entity_discount_detail_response_instance.to_dict()
# create an instance of GetEntityDiscountDetailResponse from a dict
get_entity_discount_detail_response_form_dict = get_entity_discount_detail_response.from_dict(get_entity_discount_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


