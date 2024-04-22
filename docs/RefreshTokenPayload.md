# RefreshTokenPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_token** | **str** |  | 
**refresh_token** | **str** |  | 

## Example

```python
from hyperstack.models.refresh_token_payload import RefreshTokenPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshTokenPayload from a JSON string
refresh_token_payload_instance = RefreshTokenPayload.from_json(json)
# print the JSON string representation of the object
print(RefreshTokenPayload.to_json())

# convert the object into a dict
refresh_token_payload_dict = refresh_token_payload_instance.to_dict()
# create an instance of RefreshTokenPayload from a dict
refresh_token_payload_form_dict = refresh_token_payload.from_dict(refresh_token_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


