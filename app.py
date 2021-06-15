from flask import Flask,request,jsonify,render_template
import json
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/route1',methods=['POST','GET'])
def route1():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}