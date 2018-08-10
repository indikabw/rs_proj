FROM	prom/prometheus
ADD		config/prometheus.yml /etc/prometheus/

EXPOSE 9090
