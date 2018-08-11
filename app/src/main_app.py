#	Author: Indika Wijayasinghe
#	Email: i.b.wijayasinghe@ieee.org
#
#	Description: Service fetches bitcoin price from bitstamp
#							 every 15s, and exposes the metric to prometheus
#							 to be stored.

from prometheus_client import start_http_server, Gauge
import time, httplib, json

# Connection to Bitstamp API.
conn = httplib.HTTPSConnection("api.coinbase.com")

# Create a metric to track bitcoin price.
bv = Gauge('bitcoin_value', 'Bitcoin Price Index')

if __name__ == '__main__':
	# Start up the server to expose the metrics.
	start_http_server(8000)

	# Hold previous value
	prev = 0

	# Generate requests 15 seconds.
	while True:
		conn.request("GET", "/v2/prices/spot?currency=USD")
		r = conn.getresponse()
		r_dict = json.loads(r.read())

		try:
			curr = r_dict["data"]["amount"]
		except:
			curr = prev

		bv.set(curr)
		prev = curr
		time.sleep(15)

