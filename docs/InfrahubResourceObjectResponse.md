# InfrahubResourceObjectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**infrahub_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**resources** | [**List[PricebookResourceObjectResponse]**](PricebookResourceObjectResponse.md) |  | [optional] 
**price** | **float** |  | [optional] 
**actual_price** | **float** |  | [optional] 
**host_price** | **float** |  | [optional] 
**actual_host_price** | **float** |  | [optional] 
**nexgen_price** | **float** |  | [optional] 
**nexgen_actual_price** | **float** |  | [optional] 

## Example

```python
from hyperstack.models.infrahub_resource_object_response import InfrahubResourceObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InfrahubResourceObjectResponse from a JSON string
infrahub_resource_object_response_instance = InfrahubResourceObjectResponse.from_json(json)
# print the JSON string representation of the object
print InfrahubResourceObjectResponse.to_json()

# convert the object into a dict
infrahub_resource_object_response_dict = infrahub_resource_object_response_instance.to_dict()
# create an instance of InfrahubResourceObjectResponse from a dict
infrahub_resource_object_response_form_dict = infrahub_resource_object_response.from_dict(infrahub_resource_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


