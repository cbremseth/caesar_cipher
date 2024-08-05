

# Overview

This microservice encrypts a given message using a Caesar cipher with a specified shift value. It handles both positive and negative shifts and supports both alphabetic and non-alphabetic characters.

# How to Run the Microservice

## Install Dependencies

Ensure you have Flask installed. If not, you can install it using pip:

`pip install Flask`

## Run the Microservice

Run the Flask application:

`python encipher.py`

By default the service runs on port 5001.

# Requesting and Receiving Data

You can request data from the microservice by making an HTTP POST request to the /encrypt_message endpoint. The request should include a JSON body with the message to be encrypted and the shift value. Note: The message to by encrypted should be a string and the shift number should be a positive or negative integer.

```python
import requests
import json

url = 'http://localhost:5000/encrypt_message'
headers = {'Content-Type': 'application/json'}
data = {
    'message': 'Hello, World!',
    'shift': 5
}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    result = response.json()
    print(f"Encrypted Message: {result['encrypted_message']}")
else:
    print(f"Error: {response.status_code}")
    print(response.json())

```

After making a request to the microservice, you will receive a JSON response containing the encrypted message or a response status code describing the error.

# UML Diagram

![uml diagram of functionality](uml_diagram.png)

# Mitigation Plan/Communication Contract

A. I implemented the encryption service for Khaled
B. The microservice is complete.
C. N/A
D. The code is available on github here: https://github.com/cbremseth/caesar_cipher 
E. I'm available for support via DM on Discord, expect a couple hour response time but it may be sooner.
F. I'd like to know as soon as possible if there's an issue using the microservice, Khaled said that he was able to get it to work already but I can make fixes if needed.
G. The only thing I am worried about is making sure that the ascii shift math is correct and that things are being encrypted correctly. I didn't have a decrypter to use so I had to do the calculations by hand and I think it's correct, but I've been wrong before.

