# GetDiscountResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**discount_entites** | [**List[DiscountFields]**](DiscountFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.get_discount_response import GetDiscountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDiscountResponse from a JSON string
get_discount_response_instance = GetDiscountResponse.from_json(json)
# print the JSON string representation of the object
print(GetDiscountResponse.to_json())

# convert the object into a dict
get_discount_response_dict = get_discount_response_instance.to_dict()
# create an instance of GetDiscountResponse from a dict
get_discount_response_form_dict = get_discount_response.from_dict(get_discount_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


