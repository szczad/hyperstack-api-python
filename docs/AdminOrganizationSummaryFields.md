# AdminOrganizationSummaryFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hyperstack.models.admin_organization_summary_fields import AdminOrganizationSummaryFields

# TODO update the JSON string below
json = "{}"
# create an instance of AdminOrganizationSummaryFields from a JSON string
admin_organization_summary_fields_instance = AdminOrganizationSummaryFields.from_json(json)
# print the JSON string representation of the object
print(AdminOrganizationSummaryFields.to_json())

# convert the object into a dict
admin_organization_summary_fields_dict = admin_organization_summary_fields_instance.to_dict()
# create an instance of AdminOrganizationSummaryFields from a dict
admin_organization_summary_fields_form_dict = admin_organization_summary_fields.from_dict(admin_organization_summary_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


