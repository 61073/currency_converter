from unittest import TestCase
from unittest.mock import patch, Mock
import requests
from src.app.converter import CurrencyConverter
from src.exceptions.converter_exceptions import CurrencyNotFoundError, ApiDataError

success_response_eur = {
    "rates": {
        "EUR": 1.1390754045
    },
    "base": "GBP",
    "date": "2021-01-01"
}

error_response_eur = {
    "error": "Symbols 'EURO' are invalid for date 2021-02-08."
}


class TestCurrencyConverter(TestCase):

    # mock the API endpoint to give 1.50 conversion
    def test_convert_success(self):
        convert_class = CurrencyConverter()
        actual_result = convert_class.convert(1.50, "EUR", "GBP")
        expected_result = 2.25
        self.assertEqual(expected_result, actual_result)

    @patch.object(requests, 'get')
    def test_get_data_success(self, mock_get):
        mock_object = Mock()
        mock_get.return_value = mock_object
        mock_object.json.return_value = success_response_eur
        # mock request and response above
        convert_class = CurrencyConverter()
        actual_result = convert_class._get_conversion_rate("EUR")
        expected_result = 1.1390754045
        self.assertEqual(expected_result, actual_result)

    @patch.object(requests, 'get')
    def test_get_data_error_response(self, mock_get):
        mock_object = Mock()
        mock_get.return_value = mock_object
        mock_object.json.return_value = error_response_eur
        # mock request and response above
        with self.assertRaises(ApiDataError):
            convert_class = CurrencyConverter()
            convert_class._get_conversion_rate("EUR")

    @patch.object(requests, 'get')
    def test_get_data_currency_not_found(self, mock_get):
        mock_object = Mock()
        mock_get.return_value = mock_object
        mock_object.json.return_value = success_response_eur
        # mock request and response above
        with self.assertRaises(CurrencyNotFoundError):
            convert_class = CurrencyConverter()
            convert_class._get_conversion_rate("USD")

