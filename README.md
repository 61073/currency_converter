# Currency Converter

## Purpose
The purpose of this application is to be a simple project to demonstrate some of my abilities. 
This is not intended to be overly complex but to give a general idea of how I work.

## Overview
This application will give a list of currency options, and then allow an input value to be converted.
Currency rates are determined from an API from [exchangeratesapi.io](http://exchangeratesapi.io).

Current version of this application is back end logic, future update will include front end.

## Tools and languages
- Python 3.7 - for code development and unit testing
- pytest - framework for unit testing
- nose2 - library used as unit test runner
- PEP 8 - python coding style followed

## Guide
The following make commands can be used in the command line:
- `make requirements` : uses pip to install the various packages within the requirements.txt file (this command is 
ran at the start of the other make commands below)
- `make unittest` : uses nose2 and pytest to run all the unit tests within the repository
- `make cov` : uses nose2 and pytest to run all the unit tests within the repository and also gives the coverage 
of the code
- `make covhtml` : uses nose2 and pytest to run all the unit tests within the repository and also gives the coverage 
of the code in a html format which is opened in firefox

## Conversion rules
The rounding of currency is based on official guidelines, 
[link provided here](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=LEGISSUM:l25025).
Based on which the following rules are taken for rounding conversion calculations.

- Monetary amounts converted into a national currency unit must be rounded up or down to the nearest sub-unit or in 
the absence of a sub-unit to the nearest unit.
- If the application of the conversion rate gives a result which is exactly half-way, the sum is rounded up.