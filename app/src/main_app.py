#	Author: Indika Wijayasinghe
#	Email: i.b.wijayasinghe@ieee.org
#
#	Description: Service fetches bitcoin price from bitstamp
#							 every 15s, and exposes the metric to prometheus
#							 to be stored.

from prometheus_client import start_http_server, Gauge
import time, httplib, json

# Connection to Bitstamp API.
conn = httplib.HTTPSConnection("www.bitstamp.net")

# Create a metric to track bitcoin price.
bv = Gauge('bitcoin_value', 'Bitcoin Price Index')

if __name__ == '__main__':
	# Start up the server to expose the metrics.
	start_http_server(8000)
	# Generate requests 15 seconds.
	while True:
		conn.request("GET", "/api/ticker/")
		r = conn.getresponse()
		r_dict = json.loads(r.read())
		bv.set(r_dict["last"])
		time.sleep(15)
