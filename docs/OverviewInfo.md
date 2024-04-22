# OverviewInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**InstanceOverviewFields**](InstanceOverviewFields.md) |  | [optional] 
**container** | [**ContainerOverviewFields**](ContainerOverviewFields.md) |  | [optional] 
**volume** | [**VolumeOverviewFields**](VolumeOverviewFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.overview_info import OverviewInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OverviewInfo from a JSON string
overview_info_instance = OverviewInfo.from_json(json)
# print the JSON string representation of the object
print(OverviewInfo.to_json())

# convert the object into a dict
overview_info_dict = overview_info_instance.to_dict()
# create an instance of OverviewInfo from a dict
overview_info_form_dict = overview_info.from_dict(overview_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


