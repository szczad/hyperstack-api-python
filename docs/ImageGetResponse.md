# ImageGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 
**images** | [**List[ImageFields]**](ImageFields.md) |  | [optional] 

## Example

```python
from hyperstack.models.image_get_response import ImageGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageGetResponse from a JSON string
image_get_response_instance = ImageGetResponse.from_json(json)
# print the JSON string representation of the object
print ImageGetResponse.to_json()

# convert the object into a dict
image_get_response_dict = image_get_response_instance.to_dict()
# create an instance of ImageGetResponse from a dict
image_get_response_form_dict = image_get_response.from_dict(image_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


