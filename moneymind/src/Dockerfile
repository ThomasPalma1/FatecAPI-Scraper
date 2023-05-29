FROM python:3.8
WORKDIR /src
COPY ./src/ .
RUN pip3 install -r requirements.txt
RUN sleep 20
CMD ["python3", "main.py"]
