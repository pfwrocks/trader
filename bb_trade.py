from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

API_KEY = os.getenv('ALPACA_API_KEY')
API_SECRET = os.getenv('ALPACA_API_SECRET')

if not API_KEY or not API_SECRET:
    raise ValueError("API keys are not set in the environment variables.")

trading_client = TradingClient(API_KEY, API_SECRET)


# preparing order data
market_order_data = MarketOrderRequest(
                      symbol="BB",
                      qty=1,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.DAY
                  )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
                )