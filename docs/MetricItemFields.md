# MetricItemFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** |  | [optional] 
**columns** | **List[str]** |  | [optional] 
**data** | **List[List[object]]** |  | [optional] 

## Example

```python
from hyperstack.models.metric_item_fields import MetricItemFields

# TODO update the JSON string below
json = "{}"
# create an instance of MetricItemFields from a JSON string
metric_item_fields_instance = MetricItemFields.from_json(json)
# print the JSON string representation of the object
print(MetricItemFields.to_json())

# convert the object into a dict
metric_item_fields_dict = metric_item_fields_instance.to_dict()
# create an instance of MetricItemFields from a dict
metric_item_fields_form_dict = metric_item_fields.from_dict(metric_item_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


