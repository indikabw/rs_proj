# Project RS
Project RS fetches real-time bitcoin price from [Coinbase](https://api.coinbase.com/) and stores the data in a [Prometheus](https://prometheus.io/) time series database. The real-time data can be plotted using [Grafana](https://grafana.com/) platform for analysis. 

## Prerequisites
### Installing Docker CE
Docker CE can be installed using several methods (see [Docker Docs](https://docs.docker.com/install/linux/docker-ce/ubuntu/). Following is a easy method to install using a script.
```
curl -fsSL get.docker.com -o get-docker.sh
sh get-docker.sh
```
To run docker as non-root user, use the following command. Remember to log out and log back in for this to take effect.
```
sudo usermod -aG docker your-user
```
To test the installation, use:
```
sudo docker run hello-world
```
### Installing Docker-Compose
Docker-Compose can be installed using the following commands (reference [Docker Docs](https://docs.docker.com/compose/install/#install-compose)).
```
sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
To test the installation, use:
```
docker-compose --version
```

## Build and Run Project RS
The following docker-compose commands are used to build and run the project: (may need to sudo if proper permissions are not)
```
docker-compose up
```
## Viewing Time-Series Data in Grafana
To plot the time-series data in real-time, open a browser and visit the following address:
```
http://localhost:3000
```
Then go to dashboards and click on the 'Bitcoin Price Index Dashboard' to view the time-series data in a plot that refreshes every 15s.
