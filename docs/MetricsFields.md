# MetricsFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**MetricItemFields**](MetricItemFields.md) |  | [optional] 
**memory_usages** | [**MetricItemFields**](MetricItemFields.md) |  | [optional] 
**network_in** | [**MetricItemFields**](MetricItemFields.md) |  | [optional] 
**network_out** | [**MetricItemFields**](MetricItemFields.md) |  | [optional] 
**disk_read** | [**MetricItemFields**](MetricItemFields.md) |  | [optional] 
**disk_write** | [**MetricItemFields**](MetricItemFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.metrics_fields import MetricsFields

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsFields from a JSON string
metrics_fields_instance = MetricsFields.from_json(json)
# print the JSON string representation of the object
print(MetricsFields.to_json())

# convert the object into a dict
metrics_fields_dict = metrics_fields_instance.to_dict()
# create an instance of MetricsFields from a dict
metrics_fields_form_dict = metrics_fields.from_dict(metrics_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


