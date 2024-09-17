import unittest
import requests


from captcha_reader import read_captcha
from unittest.mock import patch, Mock


# Add this at the end of the file
class TestReadCaptcha(unittest.TestCase):
    @patch('requests.post')
    def test_read_captcha_success(self, mock_post):
        # Mock successful API response
        mock_response = Mock()
        mock_response.json.return_value = {
            'choices': [{'message': {'content': 'ABC123'}}]
        }
        mock_post.return_value = mock_response

        result = read_captcha('./captcha_test_images/captcha_test1.jpeg')
        self.assertEqual(result, 'ABC123')

    @patch('requests.post')
    def test_read_captcha_api_error(self, mock_post):
        # Mock API error
        mock_post.side_effect = requests.RequestException("API Error")

        with self.assertRaises(Exception) as context:
            read_captcha('./captcha_test_images/captcha_test1.jpeg')
        self.assertIn("API request failed", str(context.exception))


if __name__ == '__main__':
    unittest.main()
