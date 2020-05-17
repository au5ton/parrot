# Dockerfile
FROM python:3.8-slim
COPY * /opt/parrot/
RUN python3 setup.py install
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "server:app"]