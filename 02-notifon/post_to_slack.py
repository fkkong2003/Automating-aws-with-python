# coding: utf-8
import requests
url = '' # Replace with slack webhook URL
data = { "text": "Hello Heavenly Father."}
requests.post(url, json=data)
