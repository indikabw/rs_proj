from prometheus_client import start_http_server, Gauge
import time, httplib, json

# Connection to the CoinDesk Bitcoin Price Index API
conn = httplib.HTTPSConnection("api.coindesk.com")

# Create a metric to track bitcoin price.
tv = Gauge('bitcoin_value', 'Bitcoin Price Index')

if __name__ == '__main__':
	# Start up the server to expose the metrics.
	start_http_server(8000)
	# Generate requests each minute.
	while True:
		conn.request("GET", "/v1/bpi/currentprice.json")
		r = conn.getresponse()
		r_dict = json.loads(r.read())
		tv.set(r_dict["bpi"]["USD"]["rate_float"])
		time.sleep(60)
