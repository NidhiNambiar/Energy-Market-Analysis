from google.cloud import storage
import requests
import os
from datetime import datetime
from flask import escape

def fetch_and_store_stock_data(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    # You can use request_json or request_args to customize behavior via the request.

    # Set up authentication
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "a537c1d5b80146b121346edfca8523fbe9ff83ae"

    # Initialize Cloud Storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket('shel_stocks')

    # Function to fetch stock market data
    api_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=SHEL&interval=5min&apikey=UI2DV21Y4OL20HW6"
    response = requests.get(api_url)
    data = response.text

    filename = f"stock_data_{datetime.now()}.json"

    blob = bucket.blob(filename)
    blob.upload_from_string(data, content_type='application/json')
    return f"File {filename} uploaded to {bucket.name}."
