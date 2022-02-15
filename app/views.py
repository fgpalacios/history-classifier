from flask import escape

from flask import Flask, jsonify, request, Response, abort
import json
from app.predictor_classification_v1 import run_predictor

from app import app
'''Routes'''
@app.route('/', methods=['GET'])
def home():
    response = Response(
        response=json.dumps({'status':'publications classifier running ok'}), status=200, mimetype='application/json'
    )
    return response

@app.route('/predictor', methods=['POST'])
def api_predictor():
    # request the input parameter
    input_text = request.json.get('input_text',None)
    if not input_text:
        return abort(400, 'Missing input_text parameter')
    
    # Run predictor code
    pred = run_predictor(input_text)

    response = Response(
        response=pred, status=200, mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)