# ImportKeypairResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**keypair** | [**KeypairFields**](KeypairFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.import_keypair_response import ImportKeypairResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportKeypairResponse from a JSON string
import_keypair_response_instance = ImportKeypairResponse.from_json(json)
# print the JSON string representation of the object
print ImportKeypairResponse.to_json()

# convert the object into a dict
import_keypair_response_dict = import_keypair_response_instance.to_dict()
# create an instance of ImportKeypairResponse from a dict
import_keypair_response_form_dict = import_keypair_response.from_dict(import_keypair_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


