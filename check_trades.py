from oandapyV20 import API
import oandapyV20.endpoints.trades as trades

api = API(access_token="1e78ca9d63d08b861f5c4fc761378220-eb4444bd63d446604c955b9b2527b2ed")

accountID = "101-001-29276802-001"

r = trades.TradesList(accountID)
print("r: ", r)
rv = api.request(r)
print("rv: ", rv)
