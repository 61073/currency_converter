# Standard python imports
import requests

# Third party library imports
from unittest import TestCase
from unittest.mock import patch, Mock
from nose2.tools import params

# Local imports
from src.app.converter import CurrencyConverter
from src.exceptions.converter_exceptions import CurrencyNotFoundError, ApiDataError

success_response_eur = {
    "rates": {
        "EUR": 1.25
    },
    "base": "GBP",
    "date": "2021-01-01"
}

error_response_eur = {
    "error": "Symbols 'EURO' are invalid for date 2021-02-08."
}


class TestCurrencyConverter(TestCase):

    # Mock the API endpoint response. Params method used to test multiple value inputs and outputs.
    # Must test if output is rounded up if had 0.005 calculation result. E.g. 2.50 * 1.25 = 3.125 -> 3.13
    @patch.object(requests, 'get')
    @params((2.50, 3.13), (5.99, 7.49), (0.75, 0.94), (518.00, 647.50), (1000.00, 1250.00), (939.30, 1174.13))
    def test_convert_success(self, input_value, expected_result, mock_get):
        mock_object = Mock()
        mock_get.return_value = mock_object
        mock_object.json.return_value = success_response_eur
        # mock request and response above
        convert_class = CurrencyConverter()
        actual_result = convert_class.convert(input_value, "EUR", "GBP")
        self.assertEqual(expected_result, actual_result)

    @patch.object(requests, 'get')
    def test_get_data_success(self, mock_get):
        mock_object = Mock()
        mock_get.return_value = mock_object
        mock_object.json.return_value = success_response_eur
        # mock request and response above
        convert_class = CurrencyConverter()
        actual_result = convert_class._get_conversion_rate("EUR")
        expected_result = 1.25
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

