import os
import unittest
import requests

# AppTest: Class for app unit tests
class AppTest(unittest.TestCase):

    # Unit Test for /logs endpoint
    def test_logs_endpoint(self):
        # Invoke HTTP GET for /logs endpoint
        url = 'http://127.0.0.1:8080/logs?type=predict'
        response = requests.get(url)

        # Assert endpoint returns non-empty data
        self.assertTrue('data' in response.json())

    # Unit Test for /predict endpoint
    def test_predict_endpoint(self):
        # Invoke HTTP GET for /predict endpoint
        url = 'http://127.0.0.1:8080/predict?date=2018-01-01&country=united_kingdom'
        response = requests.get(url)

        # Assert endpoint return non-empty data
        self.assertTrue('data' in response.json())
