import os
import unittest
from src.model import model_train, model_predict

# ModelTest: Class for model unit tests
class ModelTest(unittest.TestCase):

    # Unit Test for model train
    def test_model_train(self):
        MODEL_FILE_UNITED_KINGDOM = 'models/sl-united_kingdom-0_1.joblib'

        # Initialize model train parameters
        data_dir = os.path.join("data","cs-train")

        # Train model
        model_train(data_dir,test=True)

        # Assert model file existence
        self.assertTrue(os.path.exists(MODEL_FILE_UNITED_KINGDOM))

    # Unit Test for model predict
    def test_model_predict(self):
        # Initialize model predict parameters
        country='united_kingdom'
        year='2018'
        month='01'
        day='01'
        key = 'y_pred'

        # Get model predictions
        result = model_predict(country,year,month,day)

        # Assert model file existence
        self.assertTrue(key in result)

