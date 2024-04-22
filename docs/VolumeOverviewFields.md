# VolumeOverviewFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**using** | **int** |  | [optional] 
**cost_per_hour** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.volume_overview_fields import VolumeOverviewFields

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeOverviewFields from a JSON string
volume_overview_fields_instance = VolumeOverviewFields.from_json(json)
# print the JSON string representation of the object
print(VolumeOverviewFields.to_json())

# convert the object into a dict
volume_overview_fields_dict = volume_overview_fields_instance.to_dict()
# create an instance of VolumeOverviewFields from a dict
volume_overview_fields_form_dict = volume_overview_fields.from_dict(volume_overview_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


