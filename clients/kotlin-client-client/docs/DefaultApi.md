# DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/RobinTTYTeam/AppliedAI/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**indexPostIts**](DefaultApi.md#indexPostIts) | **POST** /indexPostIts | Detects Post-it notes and digitalizes their contents

<a name="indexPostIts"></a>
# **indexPostIts**
> kotlin.Array&lt;PostIt&gt; indexPostIts(body, pictureLink)

Detects Post-it notes and digitalizes their contents

By passing in the appropriate options, you can digitalize the contents of Post-it notes 

### Example
```kotlin
// Import classes:
//import io.swagger.client.infrastructure.*
//import io.swagger.client.models.*;

val apiInstance = DefaultApi()
val body : Object =  // Object | Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.
val pictureLink : kotlin.String = pictureLink_example // kotlin.String | A link to the picture to be digitalized. Only required if no request body is provided.
try {
    val result : kotlin.Array<PostIt> = apiInstance.indexPostIts(body, pictureLink)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling DefaultApi#indexPostIts")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling DefaultApi#indexPostIts")
    e.printStackTrace()
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided. |
 **pictureLink** | **kotlin.String**| A link to the picture to be digitalized. Only required if no request body is provided. |

### Return type

[**kotlin.Array&lt;PostIt&gt;**](PostIt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: image/png
 - **Accept**: application/json

