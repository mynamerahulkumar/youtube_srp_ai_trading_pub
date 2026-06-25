from delta_rest_client import DeltaRestClient
from delta_rest_client import OrderType

# ==============================
# CONFIGURATION
# ==============================

API_KEY = "LvXcXUsCAKndMgL42vgLTXlwQXCxCf"
API_SECRET = "xu6QjLkNpgycxdzGJkGuDbDOh0LWk4wEBGUFSsyKer1yNMD5D2EV9pORykSB"

BASE_URL = "https://api.india.delta.exchange"

SYMBOL = "BTCUSD"      # BTCUSD Perpetual
SIDE = "buy"           # buy / sell
SIZE = 1               # Quantity

# ==============================
# CONNECT
# ==============================

client = DeltaRestClient(
    base_url=BASE_URL,
    api_key=API_KEY,
    api_secret=API_SECRET
)

try:

    # Fetch product details
    ticker = client.get_ticker(SYMBOL)

    product_id = ticker["product_id"]

    print("Product ID :", product_id)
    print("Mark Price :", ticker["mark_price"])

    # Place Market Order
    response = client.place_order(
        product_id=product_id,
        size=SIZE,
        side=SIDE,
        order_type=OrderType.MARKET
    )

    print("\n==============================")
    print("ORDER PLACED SUCCESSFULLY")
    print("==============================")
    print(response)

except Exception as e:
    print("\nOrder Failed")
    print(e)