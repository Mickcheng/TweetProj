FROM python:3.6

WORKDIR /app
RUN mkdir ./dataprojects
RUN mkdir ./dataprojects/model

ENV MODEL_DIR=./dataprojects/model/
ENV MODEL_FILE=model.joblib
ENV METADATA_FILE =metadata.json

ENV FLASK_APP=app.py

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


COPY docker-ml.py .
RUN python docker-ml.py


EXPOSE 5000
EXPOSE 8010

CMD ["python", "app.py"]
