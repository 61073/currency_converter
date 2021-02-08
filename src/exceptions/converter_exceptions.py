######################################################
# Converter Exceptions
######################################################


class ConverterException(Exception):
    """
    Base class for currency converter exceptions
    Subclasses should provide any of: `.default_status` and `.default_message` properties.
    """
    default_status = 1500
    default_message = "Error found while processing data for currency conversion, check logs for details"

    def __init__(self, detail=None, code=None):
        """
        Args:
            detail (str): detailed message for the Exception to be initialised with
            code (int): error code the exception is to be initialised with
        """
        super().__init__()
        if detail is None:
            detail = self.default_message
        if code is None:
            code = self.default_status

        self.detail = detail
        self.code = code

    def __str__(self):
        """
        Returns:
            returns a string representation of the exception for printing.
        """
        return f"{self.__class__.__name__}: exception_code: {self.code}; detail: {self.detail}"


class ApiDataError(ConverterException):
    """
    Inherits from base currency converter exception. Raised when error message is returned from currency rate API.
    """
    default_status = 1501
    default_message = "An error was returned while requesting external data, check logs for details"
    
    
class CurrencyNotFoundError(ConverterException):
    """
    Inherits from base currency converter exception. Raised when a specified currency is not found in the API response.
    """
    default_status = 1502
    default_message = "The currency specified could not be found in the conversion data, check that it is a " \
                      "recognised currency in the correct 3 digit format."
