# Adminrechargehistoryfields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit** | **float** |  | [optional] 
**threshold** | **float** |  | [optional] 
**prev_balance** | **float** |  | [optional] 
**curr_balance** | **float** |  | [optional] 
**medium** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.adminrechargehistoryfields import Adminrechargehistoryfields

# TODO update the JSON string below
json = "{}"
# create an instance of Adminrechargehistoryfields from a JSON string
adminrechargehistoryfields_instance = Adminrechargehistoryfields.from_json(json)
# print the JSON string representation of the object
print(Adminrechargehistoryfields.to_json())

# convert the object into a dict
adminrechargehistoryfields_dict = adminrechargehistoryfields_instance.to_dict()
# create an instance of Adminrechargehistoryfields from a dict
adminrechargehistoryfields_form_dict = adminrechargehistoryfields.from_dict(adminrechargehistoryfields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


