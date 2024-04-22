# InstancesSummaryAdmin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**instances** | [**List[InstancesSummaryFields]**](InstancesSummaryFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.instances_summary_admin import InstancesSummaryAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesSummaryAdmin from a JSON string
instances_summary_admin_instance = InstancesSummaryAdmin.from_json(json)
# print the JSON string representation of the object
print(InstancesSummaryAdmin.to_json())

# convert the object into a dict
instances_summary_admin_dict = instances_summary_admin_instance.to_dict()
# create an instance of InstancesSummaryAdmin from a dict
instances_summary_admin_form_dict = instances_summary_admin.from_dict(instances_summary_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


