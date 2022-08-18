From python:3.8.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /sample_api
WORKDIR /sample_api
ADD . /sample_api/
RUN pip install -r requirements.txt