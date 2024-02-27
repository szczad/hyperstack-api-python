# ImportKeypairPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**environment_name** | **str** |  | 
**public_key** | **str** |  | 

## Example

```python
from hyperstack.models.import_keypair_payload import ImportKeypairPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ImportKeypairPayload from a JSON string
import_keypair_payload_instance = ImportKeypairPayload.from_json(json)
# print the JSON string representation of the object
print ImportKeypairPayload.to_json()

# convert the object into a dict
import_keypair_payload_dict = import_keypair_payload_instance.to_dict()
# create an instance of ImportKeypairPayload from a dict
import_keypair_payload_form_dict = import_keypair_payload.from_dict(import_keypair_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


