//
// DefaultAPI.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation
import Alamofire


open class DefaultAPI {
    /**
     Detects Post-it notes and digitalizes their contents

     - parameter body: (body) Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided. 
     - parameter pictureLink: (query) A link to the picture to be digitalized. Only required if no request body is provided. 
     - parameter completion: completion handler to receive the data and the error objects
     */
    open class func indexPostIts(body: Object, pictureLink: String, completion: @escaping ((_ data: [PostIt]?,_ error: Error?) -> Void)) {
        indexPostItsWithRequestBuilder(body: body, pictureLink: pictureLink).execute { (response, error) -> Void in
            completion(response?.body, error)
        }
    }


    /**
     Detects Post-it notes and digitalizes their contents
     - POST /indexPostIts

     - examples: [{contentType=application/json, example=[ {
  "color" : "#aa43a0",
  "contents" : "This is the text of a Post-It.",
  "coordinates" : {
    "posX" : 17.39,
    "posY" : 83.91
  },
  "width" : 25.24,
  "id" : "d290f1ee-6c54-4b01-90e6-d701748f0851",
  "height" : 71.91
}, {
  "color" : "#aa43a0",
  "contents" : "This is the text of a Post-It.",
  "coordinates" : {
    "posX" : 17.39,
    "posY" : 83.91
  },
  "width" : 25.24,
  "id" : "d290f1ee-6c54-4b01-90e6-d701748f0851",
  "height" : 71.91
} ]}]
     - parameter body: (body) Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided. 
     - parameter pictureLink: (query) A link to the picture to be digitalized. Only required if no request body is provided. 

     - returns: RequestBuilder<[PostIt]> 
     */
    open class func indexPostItsWithRequestBuilder(body: Object, pictureLink: String) -> RequestBuilder<[PostIt]> {
        let path = "/indexPostIts"
        let URLString = SwaggerClientAPI.basePath + path
        let parameters = JSONEncodingHelper.encodingParameters(forEncodableObject: body)
        var url = URLComponents(string: URLString)
        url?.queryItems = APIHelper.mapValuesToQueryItems([
                        "pictureLink": pictureLink
        ])

        let requestBuilder: RequestBuilder<[PostIt]>.Type = SwaggerClientAPI.requestBuilderFactory.getBuilder()

        return requestBuilder.init(method: "POST", URLString: (url?.string ?? URLString), parameters: parameters, isBody: true)
    }

}
