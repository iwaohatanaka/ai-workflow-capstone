import pandas as pd
import numpy as np

from flask import Flask, request, jsonify
from datetime import datetime
from src.model import model_predict

LOG_DIR = './logs/'
# Instantiate Flask
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/logs', methods=['GET'])
def logs():
    # Check for valid type parameter
    if 'type' in request.args:
        type = request.args['type']
    else:
        return "ERROR: No type parameter specified"

    if type == 'ingest':
        # Get ingest log
        log = pd.read_csv(LOG_DIR + 'log_ingest.csv').to_dict()
    elif type == 'train':
        # Get train log
        log = pd.read_csv(LOG_DIR + 'log_train.csv').to_dict()
    elif type == 'predict':
        # Get predict log
        log = pd.read_csv(LOG_DIR + 'log_predict.csv').to_dict()
    else:
        return "ERROR: Unsupported type parameter specified = " + type

    return jsonify({
        'log': log
    })

@app.route('/predict', methods=['GET'])
def predict():
    # Check for valid date parameter
    if 'date' in request.args:
        date = request.args['date']
    else:
        return "ERROR: No date parameter specified"
    # Initialize datetime object from date parameter
    dt = datetime.strptime(date, '%Y-%m-%d')

    # Check for valid country parameter
    if 'country' in request.args:
        country = request.args['country']
    else:
        country = None

    # Check for valid duration parameter
    if 'duration' in request.args:
        duration = request.args['duration']
        if duration == '':
            duration = 30
        else:
            duration = int(duration)
    else:
        duration = 30

    # Call model with parameters
    _result = model_predict(country, str(dt.year), str(dt.month), str(dt.day))

    result = {}
    # Convert numpy objects to make them serializable
    for key,item in _result.items():
        if isinstance(item,np.ndarray):
            result[key] = item.tolist()
        else:
            result[key] = item

    # Return result
    return jsonify(result)
