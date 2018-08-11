FROM	python:2.7-slim
ADD		. /source
WORKDIR	/source

RUN pip install --trusted-host pypi.python.org -r app/conf/requirements.txt

EXPOSE	9090
EXPOSE	8000

CMD	["python", "app/src/main_app.py"]
