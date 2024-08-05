import unittest
import json
# Assuming your microservice code is in a file named microservice.py
from encipher import app


class EncryptMessageTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_encrypt_message_positive_shift(self):
        response = self.app.post('/encrypt_message', data=json.dumps(
            {'message': 'Hello, World!', 'shift': 5}), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['encrypted_message'], 'Mjqqt1%Btwqi&')

    def test_encrypt_message_negative_shift(self):
        response = self.app.post('/encrypt_message', data=json.dumps(
            {'message': 'Mjqqt1%Btwqi&', 'shift': -5}), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['encrypted_message'], 'Hello, World!')

    def test_encrypt_message_empty_string(self):
        response = self.app.post('/encrypt_message', data=json.dumps(
            {'message': '', 'shift': 5}), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['encrypted_message'], '')

    def test_encrypt_message_invalid_input(self):
        response = self.app.post('/encrypt_message', data=json.dumps(
            {'message': 12345, 'shift': 5}), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Input message must be a string.')

    def test_encrypt_message_invalid_shift(self):
        response = self.app.post('/encrypt_message', data=json.dumps(
            {'message': 'Hello, World!', 'shift': 'five'}), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Shift value must be an integer.')

    def test_encrypt_message_missing_message(self):
        response = self.app.post(
            '/encrypt_message', data=json.dumps({'shift': 5}), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data['error'], 'Invalid input. Please provide a valid string message and shift value.')

    def test_encrypt_message_missing_shift(self):
        response = self.app.post('/encrypt_message', data=json.dumps(
            {'message': 'Hello, World!'}), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            data['error'], 'Invalid input. Please provide a valid string message and shift value.')


if __name__ == '__main__':
    unittest.main()
