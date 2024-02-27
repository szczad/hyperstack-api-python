# PricebookModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**original_value** | **float** |  | [optional] 
**discount_applied** | **bool** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.pricebook_model import PricebookModel

# TODO update the JSON string below
json = "{}"
# create an instance of PricebookModel from a JSON string
pricebook_model_instance = PricebookModel.from_json(json)
# print the JSON string representation of the object
print PricebookModel.to_json()

# convert the object into a dict
pricebook_model_dict = pricebook_model_instance.to_dict()
# create an instance of PricebookModel from a dict
pricebook_model_form_dict = pricebook_model.from_dict(pricebook_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


