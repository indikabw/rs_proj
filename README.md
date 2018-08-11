# Project RS
Project RS fetches real-time bitcoin price from [Coinbase](https://api.coinbase.com/) and stores the data in a [Prometheus](https://prometheus.io/) time series database. The real-time data are plotted using [Grafana](https://grafana.com/) platform for analysis. 

## Prerequisites
### Installing Docker CE and Docker Compose
There are several methods to install Docker CE (see [Docker Docs](https://docs.docker.com/install/linux/docker-ce/ubuntu/)) and Docker Compose (see [Docker Docs](https://docs.docker.com/compose/install/#install-compose)). A configuration file is included to automate the process of installing these packages. Use this script as follows:
```
sudo ./configure
```

To test the installation of Docker CE, use:
```
sudo docker run hello-world
```

To test the installation of Docker Compose, use:
```
docker-compose --version
```

## Build and Run Project RS
Following docker-compose commands are used to build and run the project: (may need to sudo if proper permissions are not)
```
docker-compose up
```
## Viewing Time-Series Data in Grafana
To plot the time-series data in real-time, open a browser and visit the following address:
```
http://localhost:3000
```
Login with `username: admin` and `password: abc123` (admin password can be changed in grafana.yml). 

Then go to dashboards and click on the 'Bitcoin Price Index Dashboard' to view the time-series data in a plot that refreshes every 15s.
