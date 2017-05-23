import sys
from chalice import Chalice, Response

if sys.version_info[0] == 3:
    # Python 3 imports.
    from urllib.parse import urlparse, parse_qs
else:
    # Python 2 imports.
    from urlparse import urlparse, parse_qs

app = Chalice(app_name='sgms')
# unquote to enable debugging
#app.debug = True

@app.route('/')
def index():
    return Response(	body="Hello World!\n", 
			status_code=200,
			headers={'Content-Type': 'text/plain'} )

@app.route('/greeting', methods=['POST'],
           content_types=['application/x-www-form-urlencoded'])
def hello_name():
    parsed = parse_qs(app.current_request.raw_body)
    name=parsed.get('name', [])[0]
    return Response(    body='Hello ' + name + ' World!', 
                        status_code=200,
                        headers={'Content-Type': 'text/plain'} )

