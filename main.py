
# adb emu sms send 5551234 Hello Android
import json
import os
from flask import Flask, request
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'SMS TESTER ONLINE'

@app.route('/sendsms', methods=['POST'])
def sms_sender():
    request_data = request.get_json()
    message = request_data['message']
    command =  'adb emu sms send 5551234 ' + message
    os.system(command)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == '__main__':
    app.run(port=6666, debug=True)