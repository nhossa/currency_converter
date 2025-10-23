Currency Converter

This is a lightweight Python currency converter inspired by a guided project and refined through custom tweaks. Created after a recent trip abroad, this tool helps users quickly check how much their money is worth in different countries. It uses real-time exchange rate data from FreeCurrencyAPI and instantly converts a chosen currency into multiple others.

FreeCurrencyAPI is a free and reliable source for real-time foreign exchange data. The application connects to the API using a secure key stored in an environment variable.

Features

Fetches live currency data from FreeCurrencyAPI
Converts one base currency into several others at once
Uses environment variables to securely store the API key
Clean, modular code that is easy to read and extend
Suitable for travelers, students, or anyone learning about API integration in Python

Tech Stack

Language: Python
Libraries: requests, os, dotenv
API: FreeCurrencyAPI

Setup and Usage

Clone the repository:

git clone https://github.com/nhossa/currency_converter.git
cd currency_converter


Install dependencies:

pip install requests python-dotenv


Create a .env file in the project root and add your API key:

API_KEY=your_api_key_here


Run the converter:

python currency_converter.py


Follow the on-screen prompt to enter a base currency (for example: USD, EUR, SAR). The program will display the latest conversion rates for multiple currencies.

Example Output
Enter a base currency (e.g., USD): USD

1 USD equals:
3.75 SAR
0.92 EUR
132.45 JPY
1.27 CAD

Data Source

All exchange rate data is provided by FreeCurrencyAPI, a free and reliable API for live forex data.
