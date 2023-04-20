FROM python:3.8
LABEL maintainer="Thomas Palma"
WORKDIR src/
COPY src/ .
RUN pip3 install -r ./requirements.txt
CMD ["python3", "main.py"]
