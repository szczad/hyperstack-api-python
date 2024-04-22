# DeploymentFieldsforstartdeployments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**variables** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.deployment_fieldsforstartdeployments import DeploymentFieldsforstartdeployments

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentFieldsforstartdeployments from a JSON string
deployment_fieldsforstartdeployments_instance = DeploymentFieldsforstartdeployments.from_json(json)
# print the JSON string representation of the object
print(DeploymentFieldsforstartdeployments.to_json())

# convert the object into a dict
deployment_fieldsforstartdeployments_dict = deployment_fieldsforstartdeployments_instance.to_dict()
# create an instance of DeploymentFieldsforstartdeployments from a dict
deployment_fieldsforstartdeployments_form_dict = deployment_fieldsforstartdeployments.from_dict(deployment_fieldsforstartdeployments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


