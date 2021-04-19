import os
import csv
import uuid
from datetime import datetime

LOG_DIR = './logs/'
LOG_FILE_INGEST = 'log_ingest.csv'
LOG_FILE_TRAIN = 'log_train.csv'
LOG_FILE_PREDICT = 'log_predict.csv'

# Log specified data to specified log file
def log(log_dir, log_file, log_data, log_headers):
    # Initialize header flag
    header=False

    # Create log dir if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Set header flag based on log file existence
    if not os.path.exists(log_dir + log_file):
        header = True

    # Write log data
    with open(log_dir + log_file, 'a', newline='') as file:
        writer = csv.writer(file)
        if header:
            writer.writerow(log_headers)
        writer.writerow(log_data)

# Log specified ingest parameters
def update_ingest_log(x_shape):
    # Initialize timestamp
    now = datetime.now()

    # Initialize log parameters
    log_id = str(uuid.uuid4())[:8]
    log_data = list(map(str, [log_id, now, x_shape]))
    log_headers = ['log_id', 'date_time', 'x_shape']

    # Write log data
    log(LOG_DIR, LOG_FILE_INGEST, log_data, log_headers)

# Log specified train parameters
def update_train_log(tag, dates, perf, runtime, model_version, model_version_note, test):
    # Initialize timestamp
    now = datetime.now()

    # Initialize log parameters
    log_id = str(uuid.uuid4())[:8]
    log_data = list(map(str, [log_id, now, tag, dates, perf, runtime, model_version, model_version_note, test]))
    log_headers = ['log_id', 'date_time', 'tag', 'dates', 'performance', 'runtime', 'model_version', 'model_version_note', 'test']

    # Write log data
    log(LOG_DIR, LOG_FILE_TRAIN, log_data, log_headers)

# Log specified predict parameters
def update_predict_log(country, y_pred, y_proba, target_date, runtime, model_version, test):
    # Initialize timestamp
    now = datetime.now()

    # Initialize log parameters
    log_id = str(uuid.uuid4())[:8]
    log_data = list(map(str, [log_id, now, country, y_pred, y_proba, target_date, runtime, model_version, test]))
    log_headers = ['log_id', 'date_time', 'country', 'Y_pred', 'y_proba', 'target_date', 'runtime', 'model_version', 'test']

    # Write log data
    log(LOG_DIR, LOG_FILE_PREDICT, log_data, log_headers)


