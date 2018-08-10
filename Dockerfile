FROM	python:2.7-slim
ADD		. /src
WORKDIR	/src

RUN pip install --trusted-host pypi.python.org -r config/requirements.txt

EXPOSE	9090
EXPOSE	8000

CMD	["python", "src/app.py"]
