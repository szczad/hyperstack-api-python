# Adminpaymenthistoryfields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**medium** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**payment_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.adminpaymenthistoryfields import Adminpaymenthistoryfields

# TODO update the JSON string below
json = "{}"
# create an instance of Adminpaymenthistoryfields from a JSON string
adminpaymenthistoryfields_instance = Adminpaymenthistoryfields.from_json(json)
# print the JSON string representation of the object
print(Adminpaymenthistoryfields.to_json())

# convert the object into a dict
adminpaymenthistoryfields_dict = adminpaymenthistoryfields_instance.to_dict()
# create an instance of Adminpaymenthistoryfields from a dict
adminpaymenthistoryfields_form_dict = adminpaymenthistoryfields.from_dict(adminpaymenthistoryfields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


