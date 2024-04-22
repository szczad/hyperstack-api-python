# Images


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**images** | [**List[ImageGetResponse]**](ImageGetResponse.md) |  | [optional] 

## Example

```python
from hyperstack.models.images import Images

# TODO update the JSON string below
json = "{}"
# create an instance of Images from a JSON string
images_instance = Images.from_json(json)
# print the JSON string representation of the object
print(Images.to_json())

# convert the object into a dict
images_dict = images_instance.to_dict()
# create an instance of Images from a dict
images_form_dict = images.from_dict(images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


