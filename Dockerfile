FROM	prom/prometheus
ADD	prometheus.yml /etc/prometheus/

FROM	python:2.7-slim

WORKDIR	/rs_proj
ADD	. /rs_proj

CMD	["python", "src/rs_proj_main.py"]
