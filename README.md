# Project RS
Project RS fetches real-time bitcoin price from [Bitstamp](https://www.bitstamp.net/) and stores the data in a [Prometheus](https://prometheus.io/) time series database. The real-time data can be plotted using [Grafana](https://grafana.com/) platform for analysis. 

## Build and Run
The following docker-compose commands are used to build and run the project:
```
docker-compose build
docker-compose up
```
## Plotting Time-Series Data
To plot the time-series data in real-time, open a browser and visit the following address:
```
http://localhost:3000
```
Then click on the 'Bitcoin Price Index Dashboard' to view the time-series data in a plot that refreshes every 15s.
