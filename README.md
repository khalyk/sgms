## Greetings Microservice using AWS/python/chalice

This microservice was created using Chalice, a python-based serverless microframework for Amazon Web Services (AWS).

Documentation for Chalice:
http://chalice.readthedocs.io/en/latest/
Chalice GitHub repo:
https://github.com/awslabs/chalice

Chalice can be installed typically on a Linux system using:
"pip install chalice"

See the documentation above for additional details.

The microservice handles two routes including a GET request to the root (or "/") which returns a standard "Hello World!" greeting. This was implemented by the project team in the initial version of the microservice.

This new version will also handle a POST request to "/greeting" with a variable of "name" passed into the request. The following example uses the "HTTPie" utility to make a simple POST request to the endpoint:

```http --form POST https://8nd4qagt8d.execute-api.us-west-2.amazonaws.com/demo/greeting name=Kirk
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 19
Content-Type: text/plain
Date: Tue, 23 May 2017 00:42:39 GMT
Via: 1.1 20f1c35f343f4b271ae8dcacfd7ea0e9.cloudfront.net (CloudFront)
X-Amz-Cf-Id: xK3UpRkC5YA2-aeUNRLgq2N3GlxGRhfciWKSjH1RYXzTpTGV9nw9fw==
X-Amzn-Trace-Id: sampled=0;root=1-5923857e-6cccf8b6f700da16fc1ef974
X-Cache: Miss from cloudfront
x-amzn-RequestId: b8bbfa91-3f50-11e7-8f4e-67dfe1285e13

"Hello Kirk World!"
```

Chalice will allow deployments to be pushed by developers on the team to different environments (dev, test, demo, production) all with different resources:

* chalice deploy dev
* chalice deploy qa1
* chalice deploy qa2
* chalice deploy demo1
* chalice deploy demo2
* chalice deploy prod
etc.

Chalice automatically tests the code for errors before it is deployed. Should the source code contain errors, the framework will return an error message to the developer. Debugging can also be enabled by uncommenting the following line in the microservice:

app.debug = True

Amazon API Gateway provides resiliency and scalability to the application. Details can be found here:
https://aws.amazon.com/api-gateway/faqs/

Once deployed, the AWS console or API's can be used to fully manage the service versions, API caching, logs and throttling.
