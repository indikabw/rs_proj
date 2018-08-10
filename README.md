# Project RS

## Running Prometheus
```
docker run -d -p 9090:9090 -v ~/git/rs_proj/config/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/prometheus
```
