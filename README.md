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

hi
there
http --form POST https://endppointname/dev/greeting name=Test
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 19
Content-Type: text/plain
Date: Mon, 22 May 2017 23:11:05 GMT
Via: 1.1 e2af8a85927835558866752f53562ecd.cloudfront.net (CloudFront)
X-Amz-Cf-Id: JaYOEtiPSRHeGsM4R-27ihv54paYvMI84nvlkSIeHXCpK7xvrV9AAA==
X-Amzn-Trace-Id: sampled=0;root=1-59237009-fab3e8242323bf462789db69
X-Cache: Miss from cloudfront
x-amzn-RequestId: eea440aa-3f43-11e7-aa6d-8b93f65c4c72

"Hello Test World!"


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
