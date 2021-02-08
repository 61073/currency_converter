import logging
import requests

from src.exceptions.converter_exceptions import CurrencyNotFoundError, ApiDataError

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def handle_exception(error_message, exception_type):
    logger.error(f"Could not retrieve currency data due to the following error: {error_message}")
    raise exception_type(error_message)


class CurrencyConverter:

    def __init__(self):
        # default base_currency is GBP,
        self.base_currency = "GBP"

    def convert(self, input_value: float, currency_to: str, currency_from=None):
        if currency_from:
            self.base_currency = currency_from
            logger.info(f"Set base currency to {currency_from}")
        self._get_conversion_rate(currency_to)

    def _get_conversion_rate(self, currency_to: str):
        """

        Args:
            currency_to (str): 3 character code for currency to convert to e.g. "USD" or "EUR".
        """
        url = f"https://api.exchangeratesapi.io/latest?base={self.base_currency}&symbols={currency_to}"
        response = requests.get(url).json()
        rates_data = response.get("rates")
        # Maybe add a retry to this function so api is retried 2 more times.
        if not rates_data:
            error_message = response.get("error")
            handle_exception(error_message, ApiDataError)
        elif not rates_data.get(currency_to):
            error_message = f"Currency of {currency_to} could not be found in the returned Currency Data"
            handle_exception(error_message, CurrencyNotFoundError)
        return rates_data[currency_to]
