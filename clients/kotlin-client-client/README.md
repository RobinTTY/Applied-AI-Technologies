# io.swagger.client - Kotlin client library for Post-it digitalization API

## Requires

* Kotlin 1.1.2
* Gradle 3.3

## Build

First, create the gradle wrapper script:

```
gradle wrapper
```

Then, run:

```
./gradlew check assemble
```

This runs all tests and packages the library.

## Features/Implementation Notes

* Supports JSON inputs/outputs, File inputs, and Form inputs.
* Supports collection formats for query parameters: csv, tsv, ssv, pipes.
* Some Kotlin and Java types are fully qualified to avoid conflicts with types defined in Swagger definitions.
* Implementation of ApiClient is intended to reduce method counts, specifically to benefit Android targets.

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/RobinTTYTeam/AppliedAI/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**indexPostIts**](docs/DefaultApi.md#indexpostits) | **POST** /indexPostIts | Detects Post-it notes and digitalizes their contents

<a name="documentation-for-models"></a>
## Documentation for Models

 - [io.swagger.client.models.Coordinate](docs/Coordinate.md)
 - [io.swagger.client.models.PostIt](docs/PostIt.md)

<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
