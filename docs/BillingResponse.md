# BillingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**calculated_bills** | [**List[OrganizationObjectResponse]**](OrganizationObjectResponse.md) |  | [optional] 

## Example

```python
from hyperstack.models.billing_response import BillingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BillingResponse from a JSON string
billing_response_instance = BillingResponse.from_json(json)
# print the JSON string representation of the object
print BillingResponse.to_json()

# convert the object into a dict
billing_response_dict = billing_response_instance.to_dict()
# create an instance of BillingResponse from a dict
billing_response_form_dict = billing_response.from_dict(billing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


