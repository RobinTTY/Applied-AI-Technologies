/*
 * Post-it digitalization API
 * Post-it digitalization API
 *
 * OpenAPI spec version: 1.0.0
 * Contact: muellerobin95@gmail.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.api;

import io.swagger.client.ApiCallback;
import io.swagger.client.ApiClient;
import io.swagger.client.ApiException;
import io.swagger.client.ApiResponse;
import io.swagger.client.Configuration;
import io.swagger.client.Pair;
import io.swagger.client.ProgressRequestBody;
import io.swagger.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import io.swagger.client.model.PostIt;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DefaultApi {
    private ApiClient apiClient;

    public DefaultApi() {
        this(Configuration.getDefaultApiClient());
    }

    public DefaultApi(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return apiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.apiClient = apiClient;
    }

    /**
     * Build call for indexPostIts
     * @param body Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided. (required)
     * @param pictureLink A link to the picture to be digitalized. Only required if no request body is provided. (required)
     * @param progressListener Progress listener
     * @param progressRequestListener Progress request listener
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     */
    public com.squareup.okhttp.Call indexPostItsCall(Object body, String pictureLink, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        Object localVarPostBody = body;
        
        // create path and map variables
        String localVarPath = "/indexPostIts";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        if (pictureLink != null)
        localVarQueryParams.addAll(apiClient.parameterToPair("pictureLink", pictureLink));

        Map<String, String> localVarHeaderParams = new HashMap<String, String>();

        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json"
        };
        final String localVarAccept = apiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) localVarHeaderParams.put("Accept", localVarAccept);

        final String[] localVarContentTypes = {
            "image/png"
        };
        final String localVarContentType = apiClient.selectHeaderContentType(localVarContentTypes);
        localVarHeaderParams.put("Content-Type", localVarContentType);

        if(progressListener != null) {
            apiClient.getHttpClient().networkInterceptors().add(new com.squareup.okhttp.Interceptor() {
                @Override
                public com.squareup.okhttp.Response intercept(com.squareup.okhttp.Interceptor.Chain chain) throws IOException {
                    com.squareup.okhttp.Response originalResponse = chain.proceed(chain.request());
                    return originalResponse.newBuilder()
                    .body(new ProgressResponseBody(originalResponse.body(), progressListener))
                    .build();
                }
            });
        }

        String[] localVarAuthNames = new String[] {  };
        return apiClient.buildCall(localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarAuthNames, progressRequestListener);
    }
    
    @SuppressWarnings("rawtypes")
    private com.squareup.okhttp.Call indexPostItsValidateBeforeCall(Object body, String pictureLink, final ProgressResponseBody.ProgressListener progressListener, final ProgressRequestBody.ProgressRequestListener progressRequestListener) throws ApiException {
        // verify the required parameter 'body' is set
        if (body == null) {
            throw new ApiException("Missing the required parameter 'body' when calling indexPostIts(Async)");
        }
        // verify the required parameter 'pictureLink' is set
        if (pictureLink == null) {
            throw new ApiException("Missing the required parameter 'pictureLink' when calling indexPostIts(Async)");
        }
        
        com.squareup.okhttp.Call call = indexPostItsCall(body, pictureLink, progressListener, progressRequestListener);
        return call;

        
        
        
        
    }

    /**
     * Detects Post-it notes and digitalizes their contents
     * By passing in the appropriate options, you can digitalize the contents of Post-it notes 
     * @param body Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided. (required)
     * @param pictureLink A link to the picture to be digitalized. Only required if no request body is provided. (required)
     * @return List&lt;PostIt&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public List<PostIt> indexPostIts(Object body, String pictureLink) throws ApiException {
        ApiResponse<List<PostIt>> resp = indexPostItsWithHttpInfo(body, pictureLink);
        return resp.getData();
    }

    /**
     * Detects Post-it notes and digitalizes their contents
     * By passing in the appropriate options, you can digitalize the contents of Post-it notes 
     * @param body Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided. (required)
     * @param pictureLink A link to the picture to be digitalized. Only required if no request body is provided. (required)
     * @return ApiResponse&lt;List&lt;PostIt&gt;&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     */
    public ApiResponse<List<PostIt>> indexPostItsWithHttpInfo(Object body, String pictureLink) throws ApiException {
        com.squareup.okhttp.Call call = indexPostItsValidateBeforeCall(body, pictureLink, null, null);
        Type localVarReturnType = new TypeToken<List<PostIt>>(){}.getType();
        return apiClient.execute(call, localVarReturnType);
    }

    /**
     * Detects Post-it notes and digitalizes their contents (asynchronously)
     * By passing in the appropriate options, you can digitalize the contents of Post-it notes 
     * @param body Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided. (required)
     * @param pictureLink A link to the picture to be digitalized. Only required if no request body is provided. (required)
     * @param callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     */
    public com.squareup.okhttp.Call indexPostItsAsync(Object body, String pictureLink, final ApiCallback<List<PostIt>> callback) throws ApiException {

        ProgressResponseBody.ProgressListener progressListener = null;
        ProgressRequestBody.ProgressRequestListener progressRequestListener = null;

        if (callback != null) {
            progressListener = new ProgressResponseBody.ProgressListener() {
                @Override
                public void update(long bytesRead, long contentLength, boolean done) {
                    callback.onDownloadProgress(bytesRead, contentLength, done);
                }
            };

            progressRequestListener = new ProgressRequestBody.ProgressRequestListener() {
                @Override
                public void onRequestProgress(long bytesWritten, long contentLength, boolean done) {
                    callback.onUploadProgress(bytesWritten, contentLength, done);
                }
            };
        }

        com.squareup.okhttp.Call call = indexPostItsValidateBeforeCall(body, pictureLink, progressListener, progressRequestListener);
        Type localVarReturnType = new TypeToken<List<PostIt>>(){}.getType();
        apiClient.executeAsync(call, localVarReturnType, callback);
        return call;
    }
}
