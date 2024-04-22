# Adminpaymenthistoryresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**payments** | [**List[Adminpaymenthistoryfields]**](Adminpaymenthistoryfields.md) |  | [optional] 

## Example

```python
from hyperstack.models.adminpaymenthistoryresponse import Adminpaymenthistoryresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Adminpaymenthistoryresponse from a JSON string
adminpaymenthistoryresponse_instance = Adminpaymenthistoryresponse.from_json(json)
# print the JSON string representation of the object
print(Adminpaymenthistoryresponse.to_json())

# convert the object into a dict
adminpaymenthistoryresponse_dict = adminpaymenthistoryresponse_instance.to_dict()
# create an instance of Adminpaymenthistoryresponse from a dict
adminpaymenthistoryresponse_form_dict = adminpaymenthistoryresponse.from_dict(adminpaymenthistoryresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


