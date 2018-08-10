# Project RS

## Running Prometheus
```
docker run -d -p 9090:9090 -v $(pwd)/config/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/prometheus
```

## Running Grafana
```
docker run -d -p 3000:3000 -e "GF_SECURITY_ADMIN_PASSWORD=abc123" -v grafana-storage:/var/lib/grafana grafana/grafana
```
