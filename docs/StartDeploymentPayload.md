# StartDeploymentPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**template_id** | **int** |  | 
**variables** | **Dict[str, str]** |  | [optional] 

## Example

```python
from hyperstack.models.start_deployment_payload import StartDeploymentPayload

# TODO update the JSON string below
json = "{}"
# create an instance of StartDeploymentPayload from a JSON string
start_deployment_payload_instance = StartDeploymentPayload.from_json(json)
# print the JSON string representation of the object
print(StartDeploymentPayload.to_json())

# convert the object into a dict
start_deployment_payload_dict = start_deployment_payload_instance.to_dict()
# create an instance of StartDeploymentPayload from a dict
start_deployment_payload_form_dict = start_deployment_payload.from_dict(start_deployment_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


