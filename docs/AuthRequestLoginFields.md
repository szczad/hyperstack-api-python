# AuthRequestLoginFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 

## Example

```python
from hyperstack.models.auth_request_login_fields import AuthRequestLoginFields

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRequestLoginFields from a JSON string
auth_request_login_fields_instance = AuthRequestLoginFields.from_json(json)
# print the JSON string representation of the object
print(AuthRequestLoginFields.to_json())

# convert the object into a dict
auth_request_login_fields_dict = auth_request_login_fields_instance.to_dict()
# create an instance of AuthRequestLoginFields from a dict
auth_request_login_fields_form_dict = auth_request_login_fields.from_dict(auth_request_login_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


