# DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/RobinTTYTeam/AppliedAI/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**indexPostIts**](DefaultApi.md#indexPostIts) | **POST** /indexPostIts | Detects Post-it notes and digitalizes their contents

<a name="indexPostIts"></a>
# **indexPostIts**
> List&lt;PostIt&gt; indexPostIts(body, pictureLink)

Detects Post-it notes and digitalizes their contents

By passing in the appropriate options, you can digitalize the contents of Post-it notes 

### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DefaultApi;


DefaultApi apiInstance = new DefaultApi();
Object body = null; // Object | Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.
String pictureLink = "pictureLink_example"; // String | A link to the picture to be digitalized. Only required if no request body is provided.
try {
    List<PostIt> result = apiInstance.indexPostIts(body, pictureLink);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#indexPostIts");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided. |
 **pictureLink** | **String**| A link to the picture to be digitalized. Only required if no request body is provided. |

### Return type

[**List&lt;PostIt&gt;**](PostIt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: image/png
 - **Accept**: application/json

