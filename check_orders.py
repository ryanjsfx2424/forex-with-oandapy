import oandapyV20
import oandapyV20.endpoints.orders as orders

client = oandapyV20.API(access_token="1e78ca9d63d08b861f5c4fc761378220-eb4444bd63d446604c955b9b2527b2ed")

accountID = "101-001-29276802-001"

r = orders.OrderList(accountID)
print("r: ", r)
rv = client.request(r)
print("rv: ", rv)
