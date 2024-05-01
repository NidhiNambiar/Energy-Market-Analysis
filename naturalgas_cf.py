#Natural Gas
from google.cloud import storage
import requests
import os
from datetime import datetime
from flask import escape

def fetch_and_store_stock_data(request):
    request_json = request.get_json(silent=True)
    request_args = request.args

    # Initialize Cloud Storage client
    storage_client = storage.Client()
    bucket = storage_client.bucket('gasus_767')

    # Function to fetch stock market data
    api_url = "https://www.alphavantage.co/query?function=NATURAL_GAS&interval=daily&apikey=I1YA2VVJANR8KKLJ"
    response = requests.get(api_url)
    data = response.text

    filename = f"naturalgas_data_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"

    blob = bucket.blob(filename)
    blob.upload_from_string(data, content_type='application/json')
    return f"File {filename} uploaded to {bucket.name}."
