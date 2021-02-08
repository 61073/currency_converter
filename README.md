# Currency Converter

## Overview
This application will give a list of currency options, and then allow an input value to be converted.
Currency rates are determined from an API from [exchangeratesapi.io](http://exchangeratesapi.io).

Current version of this application is back end logic, future update will include front end.

## Tools and languages
- Python 3.7 - for code development and unit testing
- pytest - framework for unit testing
- nose2 - library used as unit test runner

## Guide
The following make commands can be used in the command line:
- `make requirements` : uses pip to install the various packages within the requirements.txt file (this command is 
ran at the start of the other make commands below)
- `make unittest` : uses nose2 and pytest to run all the unit tests within the repository
- `make cov` : uses nose2 and pytest to run all the unit tests within the repository and also gives the coverage 
of the code
- `make covhtml` : uses nose2 and pytest to run all the unit tests within the repository and also gives the coverage 
of the code in a html format which is opened in firefox

