FROM	python:2.7-slim
ADD		. /src
WORKDIR	/src

EXPOSE	9090

CMD	["python", "src/app.py"]
