# RegionPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.region_payload import RegionPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RegionPayload from a JSON string
region_payload_instance = RegionPayload.from_json(json)
# print the JSON string representation of the object
print RegionPayload.to_json()

# convert the object into a dict
region_payload_dict = region_payload_instance.to_dict()
# create an instance of RegionPayload from a dict
region_payload_form_dict = region_payload.from_dict(region_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


