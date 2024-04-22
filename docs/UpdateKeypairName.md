# UpdateKeypairName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new key pair name. | 

## Example

```python
from hyperstack.models.update_keypair_name import UpdateKeypairName

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKeypairName from a JSON string
update_keypair_name_instance = UpdateKeypairName.from_json(json)
# print the JSON string representation of the object
print(UpdateKeypairName.to_json())

# convert the object into a dict
update_keypair_name_dict = update_keypair_name_instance.to_dict()
# create an instance of UpdateKeypairName from a dict
update_keypair_name_form_dict = update_keypair_name.from_dict(update_keypair_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


