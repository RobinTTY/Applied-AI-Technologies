# Swagger\Client\DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/RobinTTYTeam/AppliedAI/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**indexPostIts**](DefaultApi.md#indexpostits) | **POST** /indexPostIts | Detects Post-it notes and digitalizes their contents

# **indexPostIts**
> \Swagger\Client\Model\PostIt[] indexPostIts($body, $picture_link)

Detects Post-it notes and digitalizes their contents

By passing in the appropriate options, you can digitalize the contents of Post-it notes

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$body = new \Swagger\Client\Model\Object(); // Object | Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.
$picture_link = "picture_link_example"; // string | A link to the picture to be digitalized. Only required if no request body is provided.

try {
    $result = $apiInstance->indexPostIts($body, $picture_link);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->indexPostIts: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Object**| Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided. |
 **picture_link** | **string**| A link to the picture to be digitalized. Only required if no request body is provided. |

### Return type

[**\Swagger\Client\Model\PostIt[]**](../Model/PostIt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: image/png
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

