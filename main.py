import flask
from flask import request, jsonify
from flask_cors import CORS
import json

app = flask.Flask(__name__)
#app.config["DEBUG"] = True
app.url_map.strict_slashes = False
CORS(app)

X_DIMENSION = int(1280/8)
Y_DIMENSION = int(720/8)

app.grid = []
for i in range(X_DIMENSION):
    row = []
    for j in range(Y_DIMENSION):
      row.append([0,0,0])
    app.grid.append(row)
    row = []



@app.route('/', methods=['GET'])
def home():
    return "<h1> hello </h1>"

@app.route('/getJSON', methods=['POST'])
def setPixel():    
    info_dict = json.loads(request.form['colour'])
    for pixel in info_dict:
        x,y,col = pixel
        app.grid[x][y] = col
    dict = {"status": "ok"}
    return dict

@app.route('/last', methods=['GET'])
def idk():
    dict = {"time": "07/14/2021, 01:03:26", "delta": 77146.112815}
    return dict

@app.route('/reset', methods=['GET'])
def reset():
    app.grid = []
    for i in range(X_DIMENSION):
        row = []
        for j in range(Y_DIMENSION):
            row.append([0,0,0])
        app.grid.append(row)
        row = []
    
    dict = {"status": "ok"}
    return dict

@app.route('/refresh', methods=['GET'])
def getPixels():    
    grid = {}
    grid["leds"] = app.grid
    return grid


if __name__== '__main__':
    #app.run(host="0.0.0.0", ssl_context='adhoc', port=8080)
    app.run()