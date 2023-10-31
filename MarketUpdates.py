import yfinance as yf
from twilio.rest import Client
from datetime import datetime, timedelta

def get_stock_info(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period='2d')
    current_price = data['Close'].iloc[-1]
    prev_price = data['Close'].iloc[-2]
    percent_diff = ((current_price - prev_price) / prev_price) * 100
    return current_price, percent_diff

def send_text_message(message):
    twilio_sid = 'YOUR_TWILIO_SID'  # Replace with your Twilio SID
    twilio_auth_token = 'YOUR_TWILIO_TOKEN'  # Replace with your Twilio Auth Token
    twilio_phone_num = 'YOUR_TWILIO_PHONE_NMU'  # Replace with your Twilio phone number
    your_phone_num = 'YOUR_PHONE_NUM'  # Replace with your phone number

    client = Client(twilio_sid, twilio_auth_token)
    client.messages.create(body=message, from_=twilio_phone_num, to=your_phone_num)

def main():
    stock_symbol = 'TSLA'
    current_price, percent_diff = get_stock_info(stock_symbol)

    message = f"Current Stock Price of {current_price:.2f}\n"
    message += f"Percentage difference compared to the previous day: {percent_diff:.2f}"

    send_text_message(message)

if __name__ == "__main__":
    main()
