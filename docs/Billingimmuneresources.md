# Billingimmuneresources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | [optional] 
**resource_type** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.billingimmuneresources import Billingimmuneresources

# TODO update the JSON string below
json = "{}"
# create an instance of Billingimmuneresources from a JSON string
billingimmuneresources_instance = Billingimmuneresources.from_json(json)
# print the JSON string representation of the object
print(Billingimmuneresources.to_json())

# convert the object into a dict
billingimmuneresources_dict = billingimmuneresources_instance.to_dict()
# create an instance of Billingimmuneresources from a dict
billingimmuneresources_form_dict = billingimmuneresources.from_dict(billingimmuneresources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


