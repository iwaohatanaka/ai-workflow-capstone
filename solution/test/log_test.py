import os
import unittest

from src.logger import update_ingest_log, update_train_log, update_predict_log

# LogTest: Class for log unit tests
class LogTest(unittest.TestCase):

    # Unit Test for ingest log
    def test_update_ingest_log(self):
        # Initialize log parameters
        LOG_DIR = './logs/'
        LOG_FILE_INGEST = 'log_ingest.csv'
        log_file = LOG_DIR + LOG_FILE_INGEST
        x_shape = (2000, 10)

        # Update ingest log
        update_ingest_log(x_shape)
        # Assert log file existence
        self.assertTrue(os.path.exists(log_file))

    # Unit Test for train log
    def test_update_train_log(self):
        # Initialize log parameters
        LOG_DIR = './logs/'
        LOG_FILE_TRAIN = 'log_train.csv'
        log_file = LOG_DIR + LOG_FILE_TRAIN
        tag = 'tag1'
        dates = '2019-01-01, 2019-01-02'
        perf = {'rmse': 0.1}
        runtime = "%03d:%02d:%02d"%(9, 10, 0)
        model_version = '1.0'
        model_version_note = 'note1'
        test = True

        # Update train log
        update_train_log(tag, dates, perf, runtime, model_version, model_version_note, test)
        # Assert log file existence
        self.assertTrue(os.path.exists(log_file))

    # Unit Test for predict log
    def test_update_predict_log(self):
        # Initialize log parameters
        LOG_DIR = './logs/'
        LOG_FILE_PREDICT = 'log_predict.csv'
        log_file = LOG_DIR + LOG_FILE_PREDICT
        country = 'United States'
        y_pred = 1
        y_proba = 0.9
        target_date = '2018-01-01'
        runtime = "%03d:%02d:%02d"%(12, 10, 15)
        model_version = '1.0'
        test = True

        # Update predict log
        update_predict_log(country, y_pred, y_proba, target_date, runtime, model_version, test)
        # Assert log file existence
        self.assertTrue(os.path.exists(log_file))
