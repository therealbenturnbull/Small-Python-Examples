from flask import Flask
from flask import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route('/data/<sensor_id>',  methods = ['POST'])
def hello_world2(sensor_id):
	retval = {
	'STATUS':'OK'
	}
    return retval



@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)



if __name__ == '__main__':
    app.run()
