# get_stock_price.py
import yfinance as yf
import argparse

def get_current_price_and_time(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    hist = ticker.history(period="1d", interval="1m")
    if hist.empty:
        raise ValueError("No data found. Market may be closed.")
    
    last_row = hist.iloc[-1]
    price = last_row['Close']
    timestamp = hist.index[-1]  # This is a pandas Timestamp
    return price, timestamp

def get_exchange_rate(from_currency, to_currency):
    if from_currency == to_currency:
        return 1.0
    fx_pair = f"{from_currency}{to_currency}=X"
    fx_data = yf.Ticker(fx_pair)
    fx_hist = fx_data.history(period="1d")
    if fx_hist.empty:
        raise ValueError(f"No FX data for {from_currency} to {to_currency}")
    return fx_hist['Close'].iloc[-1]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get current stock price and time in specified currency")
    parser.add_argument("ticker", help="Stock ticker symbol, e.g., GOOG or AAPL")
    parser.add_argument("currency", help="Target currency, e.g., USD, EUR, GBP")

    args = parser.parse_args()
    ticker_symbol = args.ticker.upper()
    target_currency = args.currency.upper()

    try:
        price_usd, price_time = get_current_price_and_time(ticker_symbol)
        exchange_rate = get_exchange_rate("USD", target_currency)
        converted_price = price_usd * exchange_rate

        print(f"Ticker: {ticker_symbol}")
        print(f"Time: {price_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
        print(f"Price: {converted_price:.2f} {target_currency} (converted from {price_usd:.2f} USD)")
    except Exception as e:
        print(f"Error: {e}")
