# DiscountEntityModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** |  | [optional] 
**data** | [**List[DiscountPlanFields]**](DiscountPlanFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.discount_entity_model import DiscountEntityModel

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountEntityModel from a JSON string
discount_entity_model_instance = DiscountEntityModel.from_json(json)
# print the JSON string representation of the object
print(DiscountEntityModel.to_json())

# convert the object into a dict
discount_entity_model_dict = discount_entity_model_instance.to_dict()
# create an instance of DiscountEntityModel from a dict
discount_entity_model_form_dict = discount_entity_model.from_dict(discount_entity_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


