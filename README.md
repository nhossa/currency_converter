Currency Converter

A lightweight Python currency converter inspired by a guided project and refined through custom tweaks.
Created after a recent trip abroad, this tool helps users quickly check how much their money is worth in different countries. It fetches real-time exchange rates from the FreeCurrencyAPI
 and instantly converts a chosen currency into multiple others.

Features

 Fetches live currency data from FreeCurrencyAPI

Converts one base currency into several others at once

Uses environment variables to safely store API keys

Clean, modular code that’s easy to read and extend

Ideal for travelers, students, or anyone learning API integration in Python

Tech Stack

Language: Python

Libraries: requests, os, dotenv

API: FreeCurrencyAPI

Setup & Usage

Clone the repository:

git clone https://github.com/nhossa/currency_converter.git
cd currency_converter


Install dependencies:

pip install requests python-dotenv


Create a .env file in the project root and add your API key:

API_KEY=your_api_key_here


Run the converter:

python currency_converter.py


Follow the screen prompt to enter a base currency (e.g., USD, EUR, SAR).
The app will display current conversion rates into multiple currencies.

Example Output
Enter a base currency (e.g., USD): USD

1 USD equals:
3.75 SAR
0.92 EUR
132.45 JPY
1.27 CAD

Data Source

Exchange rate data is provided by FreeCurrencyAPI
a free and reliable API for forex data.
