FROM python:3.8
LABEL maintainer="Thomas Palma"
ENV PYTHONPATH=/app/src
WORKDIR /app/src/
COPY ./src/ .
RUN pip3 install -r ./requirements.txt
CMD ["python3", "main.py"]
