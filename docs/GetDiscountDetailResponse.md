# GetDiscountDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**discounts_entity** | [**DiscountEntityModel**](DiscountEntityModel.md) |  | [optional] 

## Example

```python
from hyperstack.models.get_discount_detail_response import GetDiscountDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDiscountDetailResponse from a JSON string
get_discount_detail_response_instance = GetDiscountDetailResponse.from_json(json)
# print the JSON string representation of the object
print(GetDiscountDetailResponse.to_json())

# convert the object into a dict
get_discount_detail_response_dict = get_discount_detail_response_instance.to_dict()
# create an instance of GetDiscountDetailResponse from a dict
get_discount_detail_response_form_dict = get_discount_detail_response.from_dict(get_discount_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


