/* 
 * Post-it digitalization API
 *
 * Post-it digitalization API
 *
 * OpenAPI spec version: 1.0.0
 * Contact: muellerobin95@gmail.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using RestSharp;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace IO.Swagger.Api
{
    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
        public interface IDefaultApi : IApiAccessor
    {
        #region Synchronous Operations
        /// <summary>
        /// Detects Post-it notes and digitalizes their contents
        /// </summary>
        /// <remarks>
        /// By passing in the appropriate options, you can digitalize the contents of Post-it notes 
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.</param>
        /// <param name="pictureLink">A link to the picture to be digitalized. Only required if no request body is provided.</param>
        /// <returns>List&lt;PostIt&gt;</returns>
        List<PostIt> IndexPostIts (Object body, string pictureLink);

        /// <summary>
        /// Detects Post-it notes and digitalizes their contents
        /// </summary>
        /// <remarks>
        /// By passing in the appropriate options, you can digitalize the contents of Post-it notes 
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.</param>
        /// <param name="pictureLink">A link to the picture to be digitalized. Only required if no request body is provided.</param>
        /// <returns>ApiResponse of List&lt;PostIt&gt;</returns>
        ApiResponse<List<PostIt>> IndexPostItsWithHttpInfo (Object body, string pictureLink);
        #endregion Synchronous Operations
        #region Asynchronous Operations
        /// <summary>
        /// Detects Post-it notes and digitalizes their contents
        /// </summary>
        /// <remarks>
        /// By passing in the appropriate options, you can digitalize the contents of Post-it notes 
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.</param>
        /// <param name="pictureLink">A link to the picture to be digitalized. Only required if no request body is provided.</param>
        /// <returns>Task of List&lt;PostIt&gt;</returns>
        System.Threading.Tasks.Task<List<PostIt>> IndexPostItsAsync (Object body, string pictureLink);

        /// <summary>
        /// Detects Post-it notes and digitalizes their contents
        /// </summary>
        /// <remarks>
        /// By passing in the appropriate options, you can digitalize the contents of Post-it notes 
        /// </remarks>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.</param>
        /// <param name="pictureLink">A link to the picture to be digitalized. Only required if no request body is provided.</param>
        /// <returns>Task of ApiResponse (List&lt;PostIt&gt;)</returns>
        System.Threading.Tasks.Task<ApiResponse<List<PostIt>>> IndexPostItsAsyncWithHttpInfo (Object body, string pictureLink);
        #endregion Asynchronous Operations
    }

    /// <summary>
    /// Represents a collection of functions to interact with the API endpoints
    /// </summary>
        public partial class DefaultApi : IDefaultApi
    {
        private IO.Swagger.Client.ExceptionFactory _exceptionFactory = (name, response) => null;

        /// <summary>
        /// Initializes a new instance of the <see cref="DefaultApi"/> class.
        /// </summary>
        /// <returns></returns>
        public DefaultApi(String basePath)
        {
            this.Configuration = new IO.Swagger.Client.Configuration { BasePath = basePath };

            ExceptionFactory = IO.Swagger.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="DefaultApi"/> class
        /// </summary>
        /// <returns></returns>
        public DefaultApi()
        {
            this.Configuration = IO.Swagger.Client.Configuration.Default;

            ExceptionFactory = IO.Swagger.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Initializes a new instance of the <see cref="DefaultApi"/> class
        /// using Configuration object
        /// </summary>
        /// <param name="configuration">An instance of Configuration</param>
        /// <returns></returns>
        public DefaultApi(IO.Swagger.Client.Configuration configuration = null)
        {
            if (configuration == null) // use the default one in Configuration
                this.Configuration = IO.Swagger.Client.Configuration.Default;
            else
                this.Configuration = configuration;

            ExceptionFactory = IO.Swagger.Client.Configuration.DefaultExceptionFactory;
        }

        /// <summary>
        /// Gets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        public String GetBasePath()
        {
            return this.Configuration.ApiClient.RestClient.BaseUrl.ToString();
        }

        /// <summary>
        /// Sets the base path of the API client.
        /// </summary>
        /// <value>The base path</value>
        [Obsolete("SetBasePath is deprecated, please do 'Configuration.ApiClient = new ApiClient(\"http://new-path\")' instead.")]
        public void SetBasePath(String basePath)
        {
            // do nothing
        }

        /// <summary>
        /// Gets or sets the configuration object
        /// </summary>
        /// <value>An instance of the Configuration</value>
        public IO.Swagger.Client.Configuration Configuration {get; set;}

        /// <summary>
        /// Provides a factory method hook for the creation of exceptions.
        /// </summary>
        public IO.Swagger.Client.ExceptionFactory ExceptionFactory
        {
            get
            {
                if (_exceptionFactory != null && _exceptionFactory.GetInvocationList().Length > 1)
                {
                    throw new InvalidOperationException("Multicast delegate for ExceptionFactory is unsupported.");
                }
                return _exceptionFactory;
            }
            set { _exceptionFactory = value; }
        }

        /// <summary>
        /// Gets the default header.
        /// </summary>
        /// <returns>Dictionary of HTTP header</returns>
        [Obsolete("DefaultHeader is deprecated, please use Configuration.DefaultHeader instead.")]
        public IDictionary<String, String> DefaultHeader()
        {
            return new ReadOnlyDictionary<string, string>(this.Configuration.DefaultHeader);
        }

        /// <summary>
        /// Add default header.
        /// </summary>
        /// <param name="key">Header field name.</param>
        /// <param name="value">Header field value.</param>
        /// <returns></returns>
        [Obsolete("AddDefaultHeader is deprecated, please use Configuration.AddDefaultHeader instead.")]
        public void AddDefaultHeader(string key, string value)
        {
            this.Configuration.AddDefaultHeader(key, value);
        }

        /// <summary>
        /// Detects Post-it notes and digitalizes their contents By passing in the appropriate options, you can digitalize the contents of Post-it notes 
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.</param>
        /// <param name="pictureLink">A link to the picture to be digitalized. Only required if no request body is provided.</param>
        /// <returns>List&lt;PostIt&gt;</returns>
        public List<PostIt> IndexPostIts (Object body, string pictureLink)
        {
             ApiResponse<List<PostIt>> localVarResponse = IndexPostItsWithHttpInfo(body, pictureLink);
             return localVarResponse.Data;
        }

        /// <summary>
        /// Detects Post-it notes and digitalizes their contents By passing in the appropriate options, you can digitalize the contents of Post-it notes 
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.</param>
        /// <param name="pictureLink">A link to the picture to be digitalized. Only required if no request body is provided.</param>
        /// <returns>ApiResponse of List&lt;PostIt&gt;</returns>
        public ApiResponse< List<PostIt> > IndexPostItsWithHttpInfo (Object body, string pictureLink)
        {
            // verify the required parameter 'body' is set
            if (body == null)
                throw new ApiException(400, "Missing required parameter 'body' when calling DefaultApi->IndexPostIts");
            // verify the required parameter 'pictureLink' is set
            if (pictureLink == null)
                throw new ApiException(400, "Missing required parameter 'pictureLink' when calling DefaultApi->IndexPostIts");

            var localVarPath = "/indexPostIts";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
                "image/png"
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (pictureLink != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "pictureLink", pictureLink)); // query parameter
            if (body != null && body.GetType() != typeof(byte[]))
            {
                localVarPostBody = this.Configuration.ApiClient.Serialize(body); // http body (model) parameter
            }
            else
            {
                localVarPostBody = body; // byte array
            }

            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) this.Configuration.ApiClient.CallApi(localVarPath,
                Method.POST, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("IndexPostIts", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<PostIt>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<PostIt>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<PostIt>)));
        }

        /// <summary>
        /// Detects Post-it notes and digitalizes their contents By passing in the appropriate options, you can digitalize the contents of Post-it notes 
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.</param>
        /// <param name="pictureLink">A link to the picture to be digitalized. Only required if no request body is provided.</param>
        /// <returns>Task of List&lt;PostIt&gt;</returns>
        public async System.Threading.Tasks.Task<List<PostIt>> IndexPostItsAsync (Object body, string pictureLink)
        {
             ApiResponse<List<PostIt>> localVarResponse = await IndexPostItsAsyncWithHttpInfo(body, pictureLink);
             return localVarResponse.Data;

        }

        /// <summary>
        /// Detects Post-it notes and digitalizes their contents By passing in the appropriate options, you can digitalize the contents of Post-it notes 
        /// </summary>
        /// <exception cref="IO.Swagger.Client.ApiException">Thrown when fails to make API call</exception>
        /// <param name="body">Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.</param>
        /// <param name="pictureLink">A link to the picture to be digitalized. Only required if no request body is provided.</param>
        /// <returns>Task of ApiResponse (List&lt;PostIt&gt;)</returns>
        public async System.Threading.Tasks.Task<ApiResponse<List<PostIt>>> IndexPostItsAsyncWithHttpInfo (Object body, string pictureLink)
        {
            // verify the required parameter 'body' is set
            if (body == null)
                throw new ApiException(400, "Missing required parameter 'body' when calling DefaultApi->IndexPostIts");
            // verify the required parameter 'pictureLink' is set
            if (pictureLink == null)
                throw new ApiException(400, "Missing required parameter 'pictureLink' when calling DefaultApi->IndexPostIts");

            var localVarPath = "/indexPostIts";
            var localVarPathParams = new Dictionary<String, String>();
            var localVarQueryParams = new List<KeyValuePair<String, String>>();
            var localVarHeaderParams = new Dictionary<String, String>(this.Configuration.DefaultHeader);
            var localVarFormParams = new Dictionary<String, String>();
            var localVarFileParams = new Dictionary<String, FileParameter>();
            Object localVarPostBody = null;

            // to determine the Content-Type header
            String[] localVarHttpContentTypes = new String[] {
                "image/png"
            };
            String localVarHttpContentType = this.Configuration.ApiClient.SelectHeaderContentType(localVarHttpContentTypes);

            // to determine the Accept header
            String[] localVarHttpHeaderAccepts = new String[] {
                "application/json"
            };
            String localVarHttpHeaderAccept = this.Configuration.ApiClient.SelectHeaderAccept(localVarHttpHeaderAccepts);
            if (localVarHttpHeaderAccept != null)
                localVarHeaderParams.Add("Accept", localVarHttpHeaderAccept);

            if (pictureLink != null) localVarQueryParams.AddRange(this.Configuration.ApiClient.ParameterToKeyValuePairs("", "pictureLink", pictureLink)); // query parameter
            if (body != null && body.GetType() != typeof(byte[]))
            {
                localVarPostBody = this.Configuration.ApiClient.Serialize(body); // http body (model) parameter
            }
            else
            {
                localVarPostBody = body; // byte array
            }

            // make the HTTP request
            IRestResponse localVarResponse = (IRestResponse) await this.Configuration.ApiClient.CallApiAsync(localVarPath,
                Method.POST, localVarQueryParams, localVarPostBody, localVarHeaderParams, localVarFormParams, localVarFileParams,
                localVarPathParams, localVarHttpContentType);

            int localVarStatusCode = (int) localVarResponse.StatusCode;

            if (ExceptionFactory != null)
            {
                Exception exception = ExceptionFactory("IndexPostIts", localVarResponse);
                if (exception != null) throw exception;
            }

            return new ApiResponse<List<PostIt>>(localVarStatusCode,
                localVarResponse.Headers.ToDictionary(x => x.Name, x => string.Join(",", x.Value)),
                (List<PostIt>) this.Configuration.ApiClient.Deserialize(localVarResponse, typeof(List<PostIt>)));
        }

    }
}