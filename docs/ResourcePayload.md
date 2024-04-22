# ResourcePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **int** |  | 
**discount_percent** | **float** |  | [optional] 
**discount_type** | **str** |  | 
**discount_amount** | **float** |  | [optional] 
**resource_count** | **int** |  | [optional] 

## Example

```python
from hyperstack.models.resource_payload import ResourcePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePayload from a JSON string
resource_payload_instance = ResourcePayload.from_json(json)
# print the JSON string representation of the object
print(ResourcePayload.to_json())

# convert the object into a dict
resource_payload_dict = resource_payload_instance.to_dict()
# create an instance of ResourcePayload from a dict
resource_payload_form_dict = resource_payload.from_dict(resource_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


