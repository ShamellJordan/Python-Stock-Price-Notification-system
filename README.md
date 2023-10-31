# Python Stock Price Notification System

This Python script fetches real-time stock price data and sends it via text message, along with the percentage change compared to the previous day's closing price.

## Installation

1. Clone this repository.

2. Install the required libraries using pip:

   ```bash
   pip install yfinance twilio or add manually

   Set up a Twilio account and obtain your Twilio SID, Auth Token, and phone numbers. Replace 'YOUR_TWILIO_SID', 'YOUR_TWILIO_TOKEN', 'YOUR_TWILIO_PHONE_NUM', and 'YOUR_PHONE_NUM' in the code with your own credentials.
   run the script 

Usage

import yfinance as yf
from twilio.rest import Client
from datetime import datetime, timedelta

Features

    Fetches real-time stock price data using Yahoo Finance (yfinance).
    Calculates the percentage change compared to the previous day's closing price.
    Sends a text message with the stock price and percentage change using Twilio.

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.   
You can further customize and expand this README to include additional details, such as explanations for how to customize the stock symbol, set up Twilio, or modify the notification messages.
