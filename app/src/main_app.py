from prometheus_client import start_http_server, Gauge
import time

# Create a metric to track time spent and requests made.
tv = Gauge('counter_value', 'Random')

my_counter = 0

if __name__ == '__main__':
	# Start up the server to expose the metrics.
	start_http_server(8000)
	# Generate some requests.
	while True:
		time.sleep(1)
		tv.set(my_counter)
		my_counter = my_counter + 1
