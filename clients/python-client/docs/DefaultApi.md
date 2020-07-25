# swagger_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/RobinTTYTeam/AppliedAI/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_post_its**](DefaultApi.md#index_post_its) | **POST** /indexPostIts | Detects Post-it notes and digitalizes their contents

# **index_post_its**
> list[PostIt] index_post_its(body, picture_link)

Detects Post-it notes and digitalizes their contents

By passing in the appropriate options, you can digitalize the contents of Post-it notes 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Object() # Object | Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.
picture_link = 'picture_link_example' # str | A link to the picture to be digitalized. Only required if no request body is provided.

try:
    # Detects Post-it notes and digitalizes their contents
    api_response = api_instance.index_post_its(body, picture_link)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->index_post_its: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided. | 
 **picture_link** | **str**| A link to the picture to be digitalized. Only required if no request body is provided. | 

### Return type

[**list[PostIt]**](PostIt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: image/png
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

