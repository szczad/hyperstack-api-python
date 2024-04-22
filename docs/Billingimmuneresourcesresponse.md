# Billingimmuneresourcesresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**List[Billingimmuneresources]**](Billingimmuneresources.md) |  | [optional] 

## Example

```python
from hyperstack.models.billingimmuneresourcesresponse import Billingimmuneresourcesresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Billingimmuneresourcesresponse from a JSON string
billingimmuneresourcesresponse_instance = Billingimmuneresourcesresponse.from_json(json)
# print the JSON string representation of the object
print(Billingimmuneresourcesresponse.to_json())

# convert the object into a dict
billingimmuneresourcesresponse_dict = billingimmuneresourcesresponse_instance.to_dict()
# create an instance of Billingimmuneresourcesresponse from a dict
billingimmuneresourcesresponse_form_dict = billingimmuneresourcesresponse.from_dict(billingimmuneresourcesresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


