# DeploymentFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.deployment_fields import DeploymentFields

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentFields from a JSON string
deployment_fields_instance = DeploymentFields.from_json(json)
# print the JSON string representation of the object
print(DeploymentFields.to_json())

# convert the object into a dict
deployment_fields_dict = deployment_fields_instance.to_dict()
# create an instance of DeploymentFields from a dict
deployment_fields_form_dict = deployment_fields.from_dict(deployment_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


