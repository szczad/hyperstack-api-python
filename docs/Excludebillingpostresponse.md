# Excludebillingpostresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**data** | [**Excludebillingpostpayload**](Excludebillingpostpayload.md) |  | [optional] 

## Example

```python
from hyperstack.models.excludebillingpostresponse import Excludebillingpostresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Excludebillingpostresponse from a JSON string
excludebillingpostresponse_instance = Excludebillingpostresponse.from_json(json)
# print the JSON string representation of the object
print(Excludebillingpostresponse.to_json())

# convert the object into a dict
excludebillingpostresponse_dict = excludebillingpostresponse_instance.to_dict()
# create an instance of Excludebillingpostresponse from a dict
excludebillingpostresponse_form_dict = excludebillingpostresponse.from_dict(excludebillingpostresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


