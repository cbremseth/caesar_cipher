import requests
import json
import argparse


def test_encrypt_message(message, shift):
    url = 'http://localhost:5000/encrypt_message'
    headers = {'Content-Type': 'application/json'}

    data = {
        'message': message,
        'shift': shift
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        result = response.json()
        print(f"Encrypted Message: {result['encrypted_message']}")
    else:
        print(f"Error: {response.status_code}")
        try:
            print(response.json())
        except json.JSONDecodeError:
            print(response.text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Encrypt a message using the Caesar cipher microservice.')
    parser.add_argument('message', type=str, help='The message to encrypt.')
    parser.add_argument('shift', type=int,
                        help='The shift value for the Caesar cipher.')

    args = parser.parse_args()

    test_encrypt_message(args.message, args.shift)
