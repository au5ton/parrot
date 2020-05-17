# Dockerfile
FROM python:3.8-slim
WORKDIR /opt/parrot
COPY * /opt/parrot/
RUN python3 setup.py install
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "server:app"]