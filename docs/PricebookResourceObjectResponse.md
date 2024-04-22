# PricebookResourceObjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**amount** | **int** |  | [optional] 
**rate** | **float** |  | [optional] 
**discounted_rate** | **float** |  | [optional] 
**price** | **float** |  | [optional] 
**actual_price** | **float** |  | [optional] 
**host_price** | **float** |  | [optional] 
**host_original_price** | **float** |  | [optional] 
**nexgen_price** | **float** |  | [optional] 
**nexgen_original_price** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.pricebook_resource_object_response import PricebookResourceObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PricebookResourceObjectResponse from a JSON string
pricebook_resource_object_response_instance = PricebookResourceObjectResponse.from_json(json)
# print the JSON string representation of the object
print(PricebookResourceObjectResponse.to_json())

# convert the object into a dict
pricebook_resource_object_response_dict = pricebook_resource_object_response_instance.to_dict()
# create an instance of PricebookResourceObjectResponse from a dict
pricebook_resource_object_response_form_dict = pricebook_resource_object_response.from_dict(pricebook_resource_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


