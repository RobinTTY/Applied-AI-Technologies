# IO.Swagger.Api.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/RobinTTYTeam/AppliedAI/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**IndexPostIts**](DefaultApi.md#indexpostits) | **POST** /indexPostIts | Detects Post-it notes and digitalizes their contents

<a name="indexpostits"></a>
# **IndexPostIts**
> List<PostIt> IndexPostIts (Object body, string pictureLink)

Detects Post-it notes and digitalizes their contents

By passing in the appropriate options, you can digitalize the contents of Post-it notes 

### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class IndexPostItsExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var body = new Object(); // Object | Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.
            var pictureLink = pictureLink_example;  // string | A link to the picture to be digitalized. Only required if no request body is provided.

            try
            {
                // Detects Post-it notes and digitalizes their contents
                List&lt;PostIt&gt; result = apiInstance.IndexPostIts(body, pictureLink);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.IndexPostIts: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided. | 
 **pictureLink** | **string**| A link to the picture to be digitalized. Only required if no request body is provided. | 

### Return type

[**List<PostIt>**](PostIt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: image/png
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
