from prometheus_client import start_http_server, Gauge
import time

my_counter = 0

# Create a metric to track time spent and requests made.
TEST_VALUE = Gauge('vault_total_conection', 'Description of gauge')

if __name__ == '__main__':
	# Start up the server to expose the metrics.
	start_http_server(8000)
	# Generate some requests.
	while True:
		time.sleep(1)
		TEST_VALUE.set(my_counter)
		my_counter = my_counter + 1
