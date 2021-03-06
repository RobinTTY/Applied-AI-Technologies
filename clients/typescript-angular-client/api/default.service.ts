/**
 * Post-it digitalization API
 * Post-it digitalization API
 *
 * OpenAPI spec version: 1.0.0
 * Contact: muellerobin95@gmail.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *//* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent }                           from '@angular/common/http';
import { CustomHttpUrlEncodingCodec }                        from '../encoder';

import { Observable }                                        from 'rxjs';

import { PostIt } from '../model/postIt';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class DefaultService {

    protected basePath = 'https://virtserver.swaggerhub.com/RobinTTYTeam/AppliedAI/1.0.0';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string, @Optional() configuration: Configuration) {
        if (basePath) {
            this.basePath = basePath;
        }
        if (configuration) {
            this.configuration = configuration;
            this.basePath = basePath || configuration.basePath || this.basePath;
        }
    }

    /**
     * @param consumes string[] mime-types
     * @return true: consumes contains 'multipart/form-data', false: otherwise
     */
    private canConsumeForm(consumes: string[]): boolean {
        const form = 'multipart/form-data';
        for (const consume of consumes) {
            if (form === consume) {
                return true;
            }
        }
        return false;
    }


    /**
     * Detects Post-it notes and digitalizes their contents
     * By passing in the appropriate options, you can digitalize the contents of Post-it notes 
     * @param body Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.
     * @param pictureLink A link to the picture to be digitalized. Only required if no request body is provided.
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public indexPostIts(body: Object, pictureLink: string, observe?: 'body', reportProgress?: boolean): Observable<Array<PostIt>>;
    public indexPostIts(body: Object, pictureLink: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Array<PostIt>>>;
    public indexPostIts(body: Object, pictureLink: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Array<PostIt>>>;
    public indexPostIts(body: Object, pictureLink: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling indexPostIts.');
        }

        if (pictureLink === null || pictureLink === undefined) {
            throw new Error('Required parameter pictureLink was null or undefined when calling indexPostIts.');
        }

        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (pictureLink !== undefined && pictureLink !== null) {
            queryParameters = queryParameters.set('pictureLink', <any>pictureLink);
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'image/png'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.request<Array<PostIt>>('post',`${this.basePath}/indexPostIts`,
            {
                body: body,
                params: queryParameters,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
