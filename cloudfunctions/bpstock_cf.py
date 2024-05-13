#BP

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
    bucket = storage_client.bucket('stock767_bp')

    # Function to fetch stock market data
    api_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BP&apikey=311DM75JHN4UE6UD"
    response = requests.get(api_url)
    data = response.text

    filename = f"stock_data_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"

    blob = bucket.blob(filename)
    blob.upload_from_string(data, content_type='application/json')
    return f"File {filename} uploaded to {bucket.name}."
