import json
import re

import requests
from flask import Flask,Blueprint, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

REQUEST_URL = "http://localhost:5005/webhooks/rest/webhook"
HEADERS = {'Content-Type': 'application/json; charset=utf-8'}

@app.route('/', methods=['GET', 'POST'])
def test():
    # return 'this a test page', 200
    return render_template('chat.html')

@app.route('/chat',methods=['GET'])
def chat():
    data=request.args.to_dict()
    message=data['message']
    if message:
        answer = rasaresponse('ssdfdf',message)
        return answer



def rasaresponse(user,msg):
    data={'sender':user,'message':msg}
    response=requests.post(REQUEST_URL, json=data,headers=HEADERS)
    if response.status_code == 200:
        data=response.json()
        if data !=[]:
            return data[0]['text']

        else:
            return "Oh, this little wit doesn't understand either"

    else:
        return 'Error returned. Please re-enter the question.'

if __name__ == '__main__':
        app.debug = True
        app.run(host='0.0.0.0', port=5000)
