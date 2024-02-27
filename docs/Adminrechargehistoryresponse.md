# Adminrechargehistoryresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**data** | [**List[Adminrechargehistoryfields]**](Adminrechargehistoryfields.md) |  | [optional] 

## Example

```python
from hyperstack.models.adminrechargehistoryresponse import Adminrechargehistoryresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Adminrechargehistoryresponse from a JSON string
adminrechargehistoryresponse_instance = Adminrechargehistoryresponse.from_json(json)
# print the JSON string representation of the object
print Adminrechargehistoryresponse.to_json()

# convert the object into a dict
adminrechargehistoryresponse_dict = adminrechargehistoryresponse_instance.to_dict()
# create an instance of Adminrechargehistoryresponse from a dict
adminrechargehistoryresponse_form_dict = adminrechargehistoryresponse.from_dict(adminrechargehistoryresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


