# UpdateEnvironment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name of the environment. | 

## Example

```python
from hyperstack.models.update_environment import UpdateEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEnvironment from a JSON string
update_environment_instance = UpdateEnvironment.from_json(json)
# print the JSON string representation of the object
print(UpdateEnvironment.to_json())

# convert the object into a dict
update_environment_dict = update_environment_instance.to_dict()
# create an instance of UpdateEnvironment from a dict
update_environment_form_dict = update_environment.from_dict(update_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


