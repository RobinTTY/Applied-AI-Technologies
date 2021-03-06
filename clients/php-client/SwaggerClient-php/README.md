# SwaggerClient-php
Post-it digitalization API

This PHP package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.php.PhpClientCodegen

## Requirements

PHP 5.5 and later

## Installation & Usage
### Composer

To install the bindings via [Composer](http://getcomposer.org/), add the following to `composer.json`:

```
{
  "repositories": [
    {
      "type": "git",
      "url": "https://github.com/GIT_USER_ID/GIT_REPO_ID.git"
    }
  ],
  "require": {
    "GIT_USER_ID/GIT_REPO_ID": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
    require_once('/path/to/SwaggerClient-php/vendor/autoload.php');
```

## Tests

To run the unit tests:

```
composer install
./vendor/bin/phpunit
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/RobinTTYTeam/AppliedAI/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**indexPostIts**](docs/Api/DefaultApi.md#indexpostits) | **POST** /indexPostIts | Detects Post-it notes and digitalizes their contents

## Documentation For Models

 - [Coordinate](docs/Model/Coordinate.md)
 - [PostIt](docs/Model/PostIt.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

muellerobin95@gmail.com

