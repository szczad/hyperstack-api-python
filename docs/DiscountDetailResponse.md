# DiscountDetailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**discount_plan** | [**List[InsertDiscountPlanFields]**](InsertDiscountPlanFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.discount_detail_response import DiscountDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountDetailResponse from a JSON string
discount_detail_response_instance = DiscountDetailResponse.from_json(json)
# print the JSON string representation of the object
print DiscountDetailResponse.to_json()

# convert the object into a dict
discount_detail_response_dict = discount_detail_response_instance.to_dict()
# create an instance of DiscountDetailResponse from a dict
discount_detail_response_form_dict = discount_detail_response.from_dict(discount_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


